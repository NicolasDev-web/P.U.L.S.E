# P.U.L.S.E. - Pipeline Unique for Reading and Epidemiological Segmentation 🩺

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-5A67D8?style=for-the-badge&logo=databricks&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

## 📋 About the Project

**P.U.L.S.E.** is a **Local RAG (Retrieval-Augmented Generation)** solution developed specifically for the Public Health niche. The system enables ingestion, vectorization, and consultation of clinical documents with precision and security, all running locally without sending data to the cloud.

## 🎯 The Business Problem

In the healthcare sector, accuracy and privacy are non-negotiable. Professionals face significant challenges:

- ❌ Difficulty consulting clinical guidelines spanning hundreds of pages in real-time
- ❌ Dependence on cloud solutions that compromise data privacy
- ❌ Lack of tools combining AI with local security

**P.U.L.S.E.** solves these problems by offering a local, secure, and efficient AI solution.

## 🧠 Solution Architecture

The application follows an adaptation of the **Medallion Architecture** for AI workflows:

| Layer | Stage | Description |
|-------|-------|-------------|
| **Bronze** | Ingestion | Automatic monitoring of directories for new PDFs and CSVs |
| **Silver** | Processing | Data cleaning with Pandas and semantic segmentation (Chunking) with LangChain |
| **Gold** | Vectorization | Embedding generation via HuggingFace and persistence in local vector database ChromaDB |
| **API** | Retrieval & Response | RAG pipeline orchestrated by LangChain consulting the **Phi-3 (Microsoft)** model via Ollama |

## 🛠️ Technology Stack

### Data Engineering
- Python 3.x
- Pandas
- Pathlib
- PDFPlumber

### Artificial Intelligence
- **LangChain** (Chains & Retrieval)
- **HuggingFace Embeddings**
- **Ollama** (Llama 3 / Phi-3)

### Database
- **ChromaDB** (Local Vector Store)

### Interface & Frontend
- **Streamlit** with custom CSS (Claude-style UI)

## 🚀 Installation Guide

### Prerequisites
- Python 3.8+
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/P.U.L.S.E.git
```

### Step 2: Create and Activate Virtual Environment

```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure AI Engine (Ollama)

1. Download Ollama from [ollama.com](https://ollama.com)
2. In the terminal, execute:

```bash
ollama run phi3
```

### Step 5: Run the Pipeline

1. Place your PDFs in `data/raw/`
2. Run the main pipeline:

```bash
python main_pipeline.py
```

3. Start the Streamlit application:

```bash
python -m streamlit run src/app/chat.py
```

The application will be available at `http://localhost:8501`

## 📁 Project Structure

```
P.U.L.S.E/
├── data/
│   ├── raw/              # PDFs and CSVs for ingestion
│   ├── processed/        # Processed data
│   └── vectors/          # Vector database (ChromaDB)
├── src/
│   ├── pipeline/         # ETL pipeline
│   ├── rag/              # RAG logic
│   └── app/              # Streamlit interface
├── main_pipeline.py      # Main script
├── requirements.txt      # Dependencies
└── README.md
```

## 💡 How to Use

1. **Add Documents:** Place PDFs in the `data/raw/` folder
2. **Process:** Run `python main_pipeline.py`
3. **Query:** Use the Streamlit interface to ask questions
4. **Get Answers:** The system returns responses based on your documents

## 🔒 Security & Privacy

- ✅ All AI runs **locally** (no data sent to the cloud)
- ✅ Data stored in **local vector database**
- ✅ Compatible with **LGPD** and healthcare regulations

## 👤 Author

**Nicolas** - [@NicolasDev-web](https://github.com/NicolasDev-web)

## 🤝 Contributing

Contributions are welcome! Feel free to open issues and pull requests.

---

**Developed with ❤️ for Public Health**

### Sources and Credits

The chatbot was developed based on the document "Clinical Protocol and Therapeutic Guidelines for Comprehensive Care of People with Sexually Transmitted Infections (STI)". This document...
