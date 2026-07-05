
# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer that runs **completely offline** using **Ollama** and **Qwen2.5**. Upload your resume in PDF format and get an instant ATS-style analysis with strengths, weaknesses, missing skills, improvement suggestions, and interview questions.

---

## 🚀 Features

- 📄 Upload Resume (PDF)
- 🤖 AI-powered Resume Analysis
- 📊 ATS Score
- 📝 Resume Summary
- ✅ Strengths & Weaknesses
- 🛠 Missing Skills
- 💡 Improvement Suggestions
- 💼 Suitable Job Roles
- ❓ Interview Questions
- 📥 Download Analysis Report
- 🔒 Runs Completely Offline using Ollama

---

## 🛠 Tech Stack

- Python
- Streamlit
- Ollama
- Qwen2.5 Model
- PyPDF2

---

## 📂 Project Structure

```
AI-Resume-Analyzer/
│
├── app.py
├── analyzer.py
├── pdf_reader.py
├── prompts.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer.git

cd AI-Resume-Analyzer
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the required model:

```bash
ollama pull qwen2.5:3b
```

Make sure Ollama is running before starting the application.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📖 How to Use

1. Launch the application.
2. Upload your Resume in PDF format.
3. Click **Analyze Resume**.
4. Wait for the AI to process the resume.
5. View the generated ATS report.
6. Download the report if needed.

---

## 📋 Analysis Includes

- ATS Score
- Resume Summary
- Strengths
- Weaknesses
- Missing Skills
- Improvement Suggestions
- Suitable Job Roles
- Interview Questions

---

## 📌 Requirements

- Python 3.10+
- Ollama
- Qwen2.5:3b Model

---

## 🔮 Future Improvements

- Multiple Resume Templates
- JD vs Resume Matching
- Resume Keyword Optimization
- Skill Gap Analysis
- Cover Letter Generator
- Export Report as PDF
- Support for DOCX Files
- Multi-language Support

---

## 🤝 Contributing

Contributions are welcome!

Feel free to fork this repository, create a new branch, and submit a Pull Request.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 📜 License

This project is licensed under the MIT License.
