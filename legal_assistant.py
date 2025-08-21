import streamlit as st
import pdfplumber
import openai
import os
from typing import Optional
import tempfile

# Configure the page
st.set_page_config(
    page_title="AI Legal Assistant - Indian Law",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize OpenAI client
@st.cache_resource
def init_openai_client():
    """Initialize OpenAI client with API key"""
    # Check for API key in environment variable first, then in secrets
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        if "openai_api_key" not in st.secrets.get("general", {}):
            st.error("Please add your OpenAI API key to .streamlit/secrets.toml")
            st.stop()
        
        api_key = st.secrets["general"]["openai_api_key"]

    return openai.OpenAI(api_key=api_key)

def extract_text_from_pdf(pdf_file) -> str:
    """Extract text from uploaded PDF file"""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(pdf_file.read())
            tmp_file_path = tmp_file.name
        
        text = ""
        with pdfplumber.open(tmp_file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        
        # Clean up temporary file
        os.unlink(tmp_file_path)
        
        return text.strip()
    except Exception as e:
        st.error(f"Error extracting text from PDF: {str(e)}")
        return ""

def get_legal_summary(client, document_text: str, model: str = "gpt-3.5-turbo") -> str:
    """Generate a legal summary of the document using OpenAI"""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": """You are a legal assistant specializing in Indian law. Your task is to summarize legal documents in plain English for non-lawyers. Focus on:
                    
                    1. Key terms and conditions
                    2. Rights and obligations of parties
                    3. Important clauses (termination, payment, liability, etc.)
                    4. Potential risks or concerns
                    5. Next steps or deadlines
                    
                    Always reference Indian legal context where applicable. Keep the summary clear, concise, and accessible. Highlight any critical legal clauses like indemnity, arbitration, termination, confidentiality, etc.
                    
                    IMPORTANT: Always include a disclaimer that this is for informational purposes only and not legal advice."""
                },
                {
                    "role": "user",
                    "content": f"Please provide a plain-English summary of this legal document:\n\n{document_text}"
                }
            ],
            max_tokens=1500,
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating summary: {str(e)}"

def get_legal_answer(client, question: str, model: str = "gpt-3.5-turbo") -> str:
    """Answer legal questions focused on Indian law"""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": """You are a legal assistant specializing in Indian law. Provide accurate, helpful information about Indian legal matters including:
                    
                    - Contract law under the Indian Contract Act, 1872
                    - Employment law and labor rights in India
                    - Property and tenancy laws
                    - Consumer protection laws
                    - Company law and business regulations
                    - Constitutional rights and civil liberties
                    
                    Always:
                    1. Focus specifically on Indian laws and regulations
                    2. Cite relevant Indian acts or legal provisions when applicable
                    3. Provide practical, actionable guidance
                    4. Include appropriate disclaimers
                    5. Avoid references to US, UK, or other foreign legal systems unless for comparison
                    
                    IMPORTANT: Always end responses with a clear disclaimer that this is general information only and not substitute for professional legal advice."""
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            max_tokens=1000,
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating answer: {str(e)}"

def main():
    # Header
    st.title("⚖️ AI Legal Assistant")
    st.subheader("Legal Document Analysis & Indian Law Q&A")
    
    # Disclaimer
    st.warning("""
    **⚠️ Disclaimer:** This tool provides general information about Indian law for educational purposes only. 
    It does not constitute legal advice and should not be relied upon for legal decisions. 
    Always consult with a qualified legal professional for specific legal matters.
    """)
    
    # Initialize OpenAI client
    client = init_openai_client()
    
    # Model selection (moved to top for accessibility)
    st.subheader("🤖 AI Model Selection")
    col_model1, col_model2 = st.columns([1, 2])
    
    with col_model1:
        model_choice = st.selectbox(
            "Choose AI Model:",
            ["gpt-3.5-turbo", "gpt-4"],
            index=0,
            help="GPT-3.5-turbo works for all accounts. GPT-4 requires paid access."
        )
    
    with col_model2:
        if model_choice == "gpt-4":
            st.info("💡 **Note**: GPT-4 requires a paid OpenAI account with API access.")
        else:
            st.success("✅ GPT-3.5-turbo works with all OpenAI accounts (free & paid).")
    
    st.divider()
    
    # Create two columns for the main features
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("📄 Document Summarizer")
        st.write("Upload a legal PDF document to get a plain-English summary")
        
        uploaded_file = st.file_uploader(
            "Choose a PDF file",
            type="pdf",
            help="Upload contracts, agreements, notices, or other legal documents"
        )
        
        if uploaded_file is not None:
            st.success(f"Uploaded: {uploaded_file.name}")
            
            if st.button("📝 Analyze Document", type="primary"):
                with st.spinner("Extracting text from PDF..."):
                    document_text = extract_text_from_pdf(uploaded_file)
                
                if not document_text:
                    st.error("❌ No text found in the PDF. Scanned documents are not supported in this demo.")
                elif len(document_text) < 50:
                    st.warning("⚠️ Very little text extracted. The document might be scanned or have formatting issues.")
                else:
                    st.success(f"✅ Extracted {len(document_text)} characters from the document")
                    
                    with st.spinner("Generating legal summary..."):
                        summary = get_legal_summary(client, document_text, model_choice)
                    
                    st.subheader("📋 Document Summary")
                    st.write(summary)
                    
                    # Show extracted text in an expander
                    with st.expander("View Extracted Text"):
                        st.text_area("Raw Text", document_text, height=300)
    
    with col2:
        st.header("❓ Legal Q&A")
        st.write("Ask questions about Indian law and get AI-generated answers")
        
        # Example questions
        st.subheader("💡 Example Questions")
        example_questions = [
            "Can my landlord evict me without notice in India?",
            "What happens if I break a contract under Indian law?",
            "What are employee rights during termination in India?",
            "What is the notice period for resignation under Indian labor law?",
            "Can a company change my salary without my consent?",
            "What are the basic rights of consumers in India?",
            "How long is the limitation period for filing a civil suit in India?",
            "What constitutes unfair trade practices under Indian law?"
        ]
        
        selected_example = st.selectbox(
            "Choose an example question:",
            [""] + example_questions,
            index=0
        )
        
        # Question input
        question = st.text_area(
            "Your Legal Question",
            value=selected_example if selected_example else "",
            height=100,
            placeholder="Ask any question about Indian law..."
        )
        
        if st.button("🔍 Get Answer", type="primary") and question:
            with st.spinner("Researching your question..."):
                answer = get_legal_answer(client, question, model_choice)
            
            st.subheader("📖 Answer")
            st.write(answer)
    
    # Sidebar with additional information
    with st.sidebar:
        st.header("ℹ️ About")
        st.write("""
        This AI Legal Assistant helps you understand legal documents and provides information about Indian law.
        
        **Features:**
        - PDF document analysis and summarization
        - Legal Q&A focused on Indian law
        - Plain-English explanations
        - Common legal clause identification
        """)
        
        st.header("🚀 Getting Started")
        st.write("""
        1. **Document Analysis**: Upload a PDF legal document to get a summary
        2. **Ask Questions**: Use the Q&A section for legal information
        3. **Examples**: Try the example questions to get started
        """)
        
        st.header("⚖️ Legal Areas Covered")
        st.write("""
        - Contract Law
        - Employment & Labor Law
        - Property & Tenancy
        - Consumer Protection
        - Company Law
        - Constitutional Rights
        - Civil & Commercial Law
        """)
        
        st.header("🔒 Privacy")
        st.write("""
        Your uploaded documents and questions are processed securely. 
        This is a demo application - avoid uploading sensitive confidential documents.
        """)

if __name__ == "__main__":
    main() 