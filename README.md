# 🩺 MediNeuron: End-to-End Medical Chatbot using Llama 2

## 📖 Project Overview

During the pandemic, I encountered the challenge of finding reliable, understandable medical information online. Motivated by this, I developed an AI-powered Medical Chatbot to provide users with accurate medical responses sourced from trusted medical encyclopedias rather than scattered online content. This project integrates Meta’s Llama 2 model with a vector database to create a domain-specific chatbot capable of answering medical queries with precision.

## ⚙️ How It Works

* **Data Ingestion**: A medical encyclopedia PDF is collected as the knowledge base.
* **Text Chunking**: The large document is split into overlapping text chunks to preserve context and fit model token limits.
* **Embeddings Creation**: Chunks are converted into embeddings using sentence-transformers.
* **Vector Database**: Embeddings are stored in Pinecone for fast similarity searches.
* **Query Handling**:

  * User queries are converted into embeddings.
  * Pinecone retrieves relevant chunks.
  * Retrieved text and the original query are fed into Llama 2 for generating context-aware answers.
* **Model Optimization**: A quantized 7B parameter version of Llama 2 is used to reduce memory requirements while maintaining accuracy.
* **Web Interface**: Built with Flask to provide an interactive user experience.

## 🌐 Tech Stack

* Python
* Meta Llama2
* LangChain
* Pinecone
* Flask
* sentence-transformers

## 🔒 Security

* API keys and sensitive information are stored in a `.env` file to ensure security and prevent accidental exposure.

## 📁 Project Structure

```
MEDICAL-CHATBOT/
│
├── data/
│   └── Medical_book.pdf               # Medical encyclopedia PDF
│
├── model/
│   └── llama-2-7b-chat.ggmlv3.q4_0.bin # Quantized Llama 2 model file
│
├── research/
│   └── trials.ipynb                   # Jupyter notebook for experiments
│
├── src/
│   ├── __init__.py
│   ├── helper.py                      # Helper functions for processing
│   ├── prompt.py                      # Prompt engineering utilities
│
├── static/
│   ├── .gitkeep
│   └── style.css                      # Custom CSS for web UI
│
├── templates/
│   └── chat.html                      # HTML template for the chat UI
│
├── venv/                              # Virtual environment
│
├── .env                               # Environment variables (Pinecone keys)
├── .gitignore                         # Git ignore file
├── LICENSE                            # MIT License file
├── app.py                             # Flask web application
├── requirements.txt                   # Project dependencies
├── setup.py                           # Setup script for packaging (if needed)
├── store_index.py                     # Script to store embeddings in Pinecone
├── template.py                        # Script for creating folder structure
└── README.md                          # Project documentation
```

## 🚀 How to Run

### Step 1: Clone the Repository

```bash
git clone https://github.com/kunalmishravitb/Medical-Chatbot.git
cd Medical-Chatbot
```

### Step 2: Create a Conda Environment

```bash
conda create -n venv python=3.10 -y
conda activate venv
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the root directory with:

```
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Step 5: Download Llama 2 Model

* Download the quantized model file:

  * `llama-2-7b-chat.ggmlv3.q4_0.bin`
  * From: [https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)
* Place the file in the `model/` directory.

### Step 6: Build the Vector Index

```bash
python store_index.py
```

### Step 7: Launch the Web Application

```bash
python app.py
```

Open your browser and navigate to:

```
http://localhost:5000
```

## 💡 Key Features

* Retrieval-augmented chatbot delivering medical information grounded in actual medical literature.
* Domain-specific insights rather than generic internet searches.
* Efficient handling of large documents using chunking and embeddings.
* Fast, scalable similarity searches via Pinecone.
* Resource-optimized deployment using quantized models.

## 🙌 Why This Matters

This project blends NLP, vector databases, and modern LLMs to make medical information more accessible and reliable. It transforms overwhelming medical research into conversational, user-friendly answers — a step toward bridging the gap between technology and human health concerns.
