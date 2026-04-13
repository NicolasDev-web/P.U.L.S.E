# P.U.L.S.E. - Pipeline Único de Leitura e Segmentação Epidemiológica 🩺

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-5A67D8?style=for-the-badge&logo=databricks&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

O **P.U.L.S.E.** é uma solução de **RAG (Retrieval-Augmented Generation) Local** desenvolvida para o nicho de Saúde Pública. O sistema permite a ingestão, vetorização e consulta de documentos técnicos densos (como PCDTs do Ministério da Saúde) de forma 100% privada e offline.

## 🎯 O Problema de Negócio
No setor de saúde, a precisão e a privacidade são inegociáveis. Profissionais enfrentam dificuldades para consultar diretrizes clínicas de centenas de páginas em tempo real. Soluções de IA em nuvem (como OpenAI) apresentam desafios de conformidade com a LGPD e custos variáveis. O P.U.L.S.E. resolve isso ao criar um cérebro digital que reside localmente na infraestrutura da instituição.

## 🧠 Arquitetura da Solução
A aplicação segue uma adaptação da **Medallion Architecture** para fluxos de IA:
1.  **Ingestão (Bronze):** Monitoramento de diretórios para novos PDFs/CSVs.
2.  **Processamento (Silver):** Limpeza de dados com Pandas e segmentação semântica (Chunking) com LangChain.
3.  **Vetorização (Gold):** Geração de embeddings via HuggingFace e persistência em banco vetorial local ChromaDB.
4.  **Recuperação & Resposta:** Pipeline RAG orquestrado pelo LangChain consultando o modelo **Phi-3 (Microsoft)** via Ollama.

## 🛠️ Stack Tecnológica
-   **Engenharia de Dados:** Python, Pandas, Pathlib, PDFPlumber.
-   **Inteligência Artificial:** LangChain (Chains & Retrival), HuggingFace Embeddings, Ollama (Llama 3/Phi-3).
-   **Banco de Dados:** ChromaDB (Vector Store).
-   **Interface:** Streamlit com injeção de CSS Customizado (Claude-like UI).

## 🚀 Como Rodar Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/P.U.L.S.E.git](https://github.com/seu-usuario/P.U.L.S.E.git)
   cd P.U.L.S.E/rag_saude_mvp
   Crie e ative o ambiente virtual:

Bash
python -m venv venv
.\venv\Scripts\activate
Instale as dependências:

Bash
pip install -r requirements.txt
Prepare o motor de IA (Ollama):

Baixe o Ollama em ollama.com.

No terminal, rode: ollama run phi3.

Inicie o Pipeline e a UI:

Coloque um PDF em data/raw/.

Execute: python main_pipeline.py

Execute: python -m streamlit run src/app/chat.py
