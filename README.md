# 📄 Enterprise PDF Q&A System using RAG + LLM

## 🚀 Overview
This project is an AI-powered Enterprise PDF Management System that enables users to upload documents and ask questions in natural language.

It leverages **Retrieval-Augmented Generation (RAG)** with **Large Language Models (LLMs)** to deliver accurate, context-aware answers from PDF documents.

---

## 🎯 Problem Statement
Organizations deal with large volumes of documents. Manually searching for information is time-consuming and inefficient.

👉 This system solves that by enabling **intelligent document querying using AI**.

---

## 🧠 Key Features
- 📂 Upload and process PDF documents  
- 🔍 Semantic search using embeddings  
- 🤖 Context-aware question answering  
- ⚡ Fast retrieval with FAISS vector database  
- 🌐 Interactive UI using Streamlit  

---

## 🏗️ System Architecture

1. Load PDF documents  
2. Split into chunks  
3. Convert text into embeddings  
4. Store embeddings in vector database (FAISS)  
5. Retrieve relevant chunks  
6. Generate answer using LLM  

---

## 🛠️ Tech Stack

- Python  
- LangChain  
- FAISS  
- OpenAI / HuggingFace  
- Streamlit  

---

## 📁 Project Structure

```
Enterprise-PDF-Q-A-System-RAG-LLM-/
│── app.py
│── requirements.txt
│── README.md
│── .env.example
│── data/
│── src/
│── notebooks/
```

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/your-username/Enterprise-PDF-Q-A-System-RAG-LLM-.git
cd Enterprise-PDF-Q-A-System-RAG-LLM-
pip install -r requirements.txt
streamlit run app.py
```

---

## 📸 Demo
(Add screenshots or GIF here)

---

## 📌 Future Improvements
- Multi-document support  
- Chat history  
- Deployment on cloud (AWS / HuggingFace)  
- Role-based access (Enterprise use-case)  

---

## 🙌 Author
**Ritik Tiwari**  
M.Tech AI & Data Science | IIT Patna  
Data Analyst @ MEA Platform Technologies  

---

## ⭐ Support
If you like this project, consider giving it a ⭐ on GitHub!
