# ⚖️ AI Legal Assistant - Indian Law

A Streamlit-based demo application that helps users understand legal documents and provides information about Indian law using AI.

## 🌟 Features

- **📄 PDF Document Analysis**: Upload legal PDFs and get plain-English summaries
- **❓ Legal Q&A**: Ask questions about Indian law and get AI-generated answers
- **🇮🇳 Indian Law Focus**: Specialized prompts and examples for Indian legal system
- **🔍 Clause Identification**: Automatically identifies common legal clauses
- **⚠️ Scanned PDF Detection**: Handles scanned documents gracefully
- **🎯 User-Friendly Interface**: Clean, intuitive Streamlit UI

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key** (choose one method):

   **Option A: Environment Variable**
   ```bash
   # Windows
   set OPENAI_API_KEY=your_api_key_here
   
   # macOS/Linux
   export OPENAI_API_KEY=your_api_key_here
   ```

   **Option B: Streamlit Secrets**
   
   Create `.streamlit/secrets.toml`:
   ```toml
   OPENAI_API_KEY = "your_api_key_here"
   ```

4. **Run the application**:
   ```bash
   streamlit run legal_assistant.py
   ```

5. **Open your browser** to `http://localhost:8501`

## 📖 Usage Guide

### Document Summarizer

1. **Upload a PDF**: Click "Choose a PDF file" and select your legal document
2. **Analyze**: Click "📝 Analyze Document" to extract and summarize the text
3. **Review**: Read the plain-English summary and identified legal clauses
4. **View Raw Text**: Expand "View Extracted Text" to see the original content

**Supported Documents:**
- Contracts and agreements
- Legal notices
- Employment documents
- Property agreements
- Any text-based PDF (scanned PDFs not supported)

### Legal Q&A

1. **Choose an Example**: Select from pre-loaded Indian law questions
2. **Ask Your Question**: Type your own legal question in the text area
3. **Get Answer**: Click "🔍 Get Answer" for AI-generated legal information
4. **Review Response**: Read the detailed answer with Indian law context

**Example Questions:**
- "Can my landlord evict me without notice in India?"
- "What happens if I break a contract under Indian law?"
- "What are employee rights during termination in India?"
- "What is the notice period for resignation under Indian labor law?"

## ⚖️ Legal Areas Covered

- **Contract Law** (Indian Contract Act, 1872)
- **Employment & Labor Law**
- **Property & Tenancy Laws**
- **Consumer Protection**
- **Company Law**
- **Constitutional Rights**
- **Civil & Commercial Law**

## 🛡️ Important Disclaimers

- **This is a demo application for educational purposes only**
- **Responses are AI-generated and may not be 100% accurate**
- **This does not constitute legal advice**
- **Always consult with qualified legal professionals for important matters**
- **Avoid uploading sensitive or confidential documents**

## 🔧 Technical Details

### Dependencies

- **Streamlit**: Web app framework
- **OpenAI**: GPT-4 for document analysis and Q&A
- **pdfplumber**: PDF text extraction
- **python-dotenv**: Environment variable management

### Architecture

- **Frontend**: Streamlit web interface
- **PDF Processing**: pdfplumber for text extraction
- **AI Engine**: OpenAI GPT-4 with specialized legal prompts
- **Context**: Focused on Indian legal system

### File Structure

```
legal-assistant/
├── legal_assistant.py    # Main Streamlit application
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🎯 Demo Limitations

This is a **demo application** with the following limitations:

- **No production-level security**: Don't upload confidential documents
- **API costs**: Uses OpenAI API (charges apply based on usage)
- **Scanned PDFs**: Cannot process image-based or scanned documents
- **Accuracy**: AI responses may contain errors or outdated information
- **Legal advice**: Does not replace professional legal consultation

## 🤝 Contributing

This is a demo project. For improvements:

1. Fork the repository
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## 📝 License

This project is for demonstration purposes. Please respect OpenAI's usage policies and terms of service.

## 🆘 Troubleshooting

### Common Issues

**"OpenAI API key not found"**
- Ensure your API key is set correctly
- Check environment variables or Streamlit secrets

**"The model gpt-4 does not exist or you do not have access to it"**
- This means you don't have GPT-4 access (most common issue)
- **Solution**: Use the model selector in the sidebar and choose "gpt-3.5-turbo"
- GPT-4 requires a paid OpenAI account with API billing set up
- GPT-3.5-turbo works with all OpenAI accounts (free and paid)

**"No text found in PDF"**
- The PDF might be scanned or image-based
- Try a different document with selectable text

**"Error extracting text"**
- The PDF might be corrupted or password-protected
- Try uploading a different file

**Slow responses**
- This is normal for GPT-4 processing
- Responses typically take 10-30 seconds

### Getting an OpenAI API Key

1. Go to [OpenAI's website](https://openai.com/api/)
2. Sign up or log in to your account
3. Navigate to API keys section
4. Create a new API key
5. Copy and use in the application

### Checking GPT-4 Access

To check if you have GPT-4 access:

1. **Free Accounts**: Only have access to GPT-3.5-turbo
2. **Paid Accounts**: Need to:
   - Add billing information
   - Make at least one successful payment
   - Wait for GPT-4 access to be enabled (usually immediate)

3. **Test Access**: Use the model selector in the app - if GPT-4 fails, switch to GPT-3.5-turbo

---

**⚠️ Remember: This tool provides general information only and is not a substitute for professional legal advice.** 