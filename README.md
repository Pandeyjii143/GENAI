# 🤖 LangChain & LLM Playground

A hands-on repository for learning and experimenting with **Large Language Models (LLMs)** using **LangChain**, **OpenAI**, and **Google Gemini**.

This repository contains simple examples that demonstrate how to interact with different LLM providers and build AI-powered applications using LangChain.

---

## 📂 Project Structure

```text
Langchain_model/
│
├── 1.LLMs/
│   └── llm_demo.py
│
├── 2.ChatModels/
│   ├── 1_chatmodel_openai.py
│   └── 2_chatmodel_googleGemini.py
│
├── .env.example
├── requirements.txt
└── README.md
```

---

## 🚀 Features

- ✅ LangChain Basics
- ✅ OpenAI Chat Models
- ✅ Google Gemini Chat Models
- ✅ Environment Variable Configuration
- ✅ Beginner-Friendly Examples
- ✅ Clean Project Structure

---

## 🛠️ Tech Stack

- Python
- LangChain
- OpenAI API
- Google Gemini API
- python-dotenv

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/Pandeyjii143/GENAI.git
```

```bash
cd GENAI
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### requirements.txt 
```
#Google Gemini (PaLM) Integration
langchain-google-genai
google-generativeai

#Hugging Face Integration
langchain-huggingface
transformers
huggingface-hub

#Environment Variable Management
python-dotenv

#MachineLearning Utilities
numpy
scikit-learn
```
### Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
```

> **Never commit your `.env` file or API keys to GitHub.**

---

## ▶️ Running Examples

### OpenAI LLM

```bash
python 1.LLMs/llm_demo.py
```

### OpenAI Chat Model

```bash
python 2.ChatModels/1_chatmodel_openai.py
```

### Google Gemini Chat Model

```bash
python 2.ChatModels/2_chatmodel_googleGemini.py
```

---

## 📚 Learning Roadmap

- [x] LLM Basics
- [x] Chat Models
- [ ] Prompt Templates
- [ ] Output Parsers
- [ ] Chains
- [ ] Runnables
- [ ] Memory
- [ ] RAG
- [ ] Agents
- [ ] LangGraph
- [ ] MCP
- [ ] Production Deployment

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Ravikishan Pandey**

- GitHub: https://github.com/Pandeyjii143
- LinkedIn: https://www.linkedin.com/in/ravikishan-pandey-872893286

---

⭐ If you find this repository helpful, consider giving it a **Star**.
