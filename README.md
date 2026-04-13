# P.U.L.S.E. - Pipeline Único de Leitura e Segmentação Epidemiológica 🩺

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=chainlink&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-5A67D8?style=for-the-badge&logo=databricks&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

## 📋 Sobre o Projeto

O **P.U.L.S.E.** é uma solução de **RAG (Retrieval-Augmented Generation) Local** desenvolvida especificamente para o nicho de Saúde Pública. O sistema permite a ingestão, vetorização e consulta inteligente de documentos clínicos e epidemiológicos com total privacidade e segurança.

## 🎯 O Problema de Negócio

No setor de saúde, a precisão e a privacidade são inegociáveis. Profissionais enfrentam desafios significativos:

- ❌ Dificuldade em consultar diretrizes clínicas de centenas de páginas em tempo real
- ❌ Dependência de soluções cloud que comprometem a privacidade dos dados
- ❌ Falta de ferramentas que combinem IA com segurança local

O **P.U.L.S.E.** resolve esses problemas oferecendo uma solução de IA local, segura e eficiente.

## 🧠 Arquitetura da Solução

A aplicação segue uma adaptação da **Medallion Architecture** para fluxos de IA:

| Camada | Etapa | Descrição |
|--------|-------|-----------|
| **Bronze** | Ingestão | Monitoramento automático de diretórios para novos PDFs e CSVs |
| **Silver** | Processamento | Limpeza de dados com Pandas e segmentação semântica (Chunking) com LangChain |
| **Gold** | Vetorização | Geração de embeddings via HuggingFace e persistência em banco vetorial local ChromaDB |
| **API** | Recuperação & Resposta | Pipeline RAG orquestrado pelo LangChain consultando o modelo **Phi-3 (Microsoft)** via Ollama |

## 🛠️ Stack Tecnológica

### Engenharia de Dados
- Python 3.x
- Pandas
- Pathlib
- PDFPlumber

### Inteligência Artificial
- **LangChain** (Chains & Retrieval)
- **HuggingFace Embeddings**
- **Ollama** (Llama 3 / Phi-3)

### Banco de Dados
- **ChromaDB** (Vector Store Local)

### Interface & Frontend
- **Streamlit** com CSS customizado (UI estilo Claude)

## 🚀 Guia de Instalação

### Pré-requisitos
- Python 3.8+
- Git

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/P.U.L.S.E.git
cd P.U.L.S.E/rag_saude_mvp
```

### Passo 2: Criar e Ativar Ambiente Virtual

```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Configurar o Motor de IA (Ollama)

1. Baixe o Ollama em [ollama.com](https://ollama.com)
2. No terminal, execute:

```bash
ollama run phi3
```

### Passo 5: Executar o Pipeline

1. Coloque seus PDFs em `data/raw/`
2. Execute o pipeline principal:

```bash
python main_pipeline.py
```

3. Inicie a aplicação Streamlit:

```bash
python -m streamlit run src/app/chat.py
```

A aplicação estará disponível em `http://localhost:8501`

## 📁 Estrutura do Projeto

```
P.U.L.S.E/
├── data/
│   ├── raw/              # PDFs e CSVs para ingestão
│   ├── processed/        # Dados processados
│   └── vectors/          # Banco de vetores (ChromaDB)
├── src/
│   ├── pipeline/         # Pipeline de ETL
│   ├── rag/              # Lógica RAG
│   └── app/              # Interface Streamlit
├── main_pipeline.py      # Script principal
├── requirements.txt      # Dependências
└── README.md
```

## 💡 Como Usar

1. **Adicionar Documentos:** Coloque PDFs na pasta `data/raw/`
2. **Processar:** Execute `python main_pipeline.py`
3. **Consultar:** Use a interface Streamlit para fazer perguntas
4. **Obter Respostas:** O sistema retorna respostas baseadas nos seus documentos

## 🔒 Segurança & Privacidade

- ✅ Toda a IA roda **localmente** (sem envio de dados à nuvem)
- ✅ Dados armazenados em **banco de dados vetorial local**
- ✅ Compatível com **LGPD** e regulamentações de saúde

## 👤 Autor

**Nicolas** - [@NicolasDev-web](https://github.com/NicolasDev-web)

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir issues e pull requests.

---

**Desenvolvido com ❤️ para Saúde Pública**
