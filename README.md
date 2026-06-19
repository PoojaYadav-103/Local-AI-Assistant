# 🤖 Local AI Assistant

A simple AI chatbot built using **Streamlit**, **LangChain**, and **Ollama (Llama 3.2)** that runs completely on a local machine. The project demonstrates how to build an LLM application using LangChain Expression Language (LCEL) and monitor its execution using LangSmith.

---

## 🚀 Features

* 💬 Interactive chat interface using Streamlit
* 🦙 Local inference with Ollama + Llama 3.2
* 🔗 LangChain prompt pipeline (LCEL)
* 📊 LangSmith tracing and monitoring
* 🎨 Clean and responsive UI
* 🔒 Runs locally without OpenAI API

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Ollama
* Llama 3.2
* LangSmith
* Python Dotenv

---

## 📂 Project Structure

```
CHATBOT/
│── app.py
│── requirements.txt
│── README.md
│── .env.example
│── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/PoojaYadav-103/Local-AI-Assistant.git
cd Local-AI-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Pull the Llama model

```bash
ollama pull llama3.2
```

### 6. Create a `.env` file

```
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=Local-AI-Assistant
```

### 7. Run the application

```bash
streamlit run app.py
```

---

## 🏗️ Architecture

```
User
   │
   ▼
Streamlit UI
   │
   ▼
ChatPromptTemplate
   │
   ▼
ChatOllama (Llama 3.2)
   │
   ▼
StrOutputParser
   │
   ▼
Response
   │
   ▼
LangSmith Tracing
```

---

## 📊 LangSmith

The application is integrated with LangSmith to visualize:

* Prompt execution
* Model response
* Execution latency
* Runnable sequence
* Debugging traces

---

## 🎯 Future Improvements

* PDF Chat (RAG)
* Website Chat
* FAISS Vector Database
* Conversation Memory
* Streaming Responses
* Multi-LLM Support

---

## 👩‍💻 Author

**Pooja Yadav**

Learning and building projects in AI, Machine Learning and LangChain.
