# 🔍 Semantic Search Mini Project

This is a minimal and elegant **semantic search application** built with **Python**, **Streamlit**, and **Docker**, using the **OpenAI API** for text embeddings and **ChromaDB** as the vector store.

It allows users to search across document content intelligently using natural language, rather than relying on exact keyword matches.

---

## 🚀 Features

- ✅ **Semantic Search** using OpenAI embeddings (`text-embedding-3-small`)
- ✅ **Chroma Vector Database** for efficient similarity search
- ✅ **Streamlit UI** for simple and intuitive search experience
- ✅ **Dockerized Setup** using Docker Compose
- ✅ Lightweight and Fast (ideal for local demos and mini-projects)

---

## 🧠 How It Works

1. Files are processed and converted into text chunks.
2. Text chunks are converted into embeddings using OpenAI API.
3. Embeddings are stored in **ChromaDB**, a persistent local vector database.
4. User types a query → query is embedded → top matches are retrieved semantically.

---

## 📦 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python + OpenAI API
- **Vector Store**: Open AI vector database 
- **Containerization**: Docker + Docker Compose

---

## 🐳 Docker Compose Setup

```bash
# Build and start the service
docker-compose up --build
