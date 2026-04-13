import streamlit as st
from pathlib import Path

# Importações do LangChain (Backend P.U.L.S.E.)
from langchain_community.chat_models import ChatOllama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA E CSS (ESTILO CLAUDE)
# ==========================================
st.set_page_config(
    page_title="P.U.L.S.E. AI", 
    page_icon="🩺", 
    layout="wide", # Layout wide para dar respiro ao texto
    initial_sidebar_state="expanded"
)

# Injeção de CSS Customizado para forçar o minimalismo
st.markdown("""
<style>
    /* Esconde elementos padrão do Streamlit para parecer um App Nativo */
    [data-testid="stHeader"] {visibility: hidden;}
    [data-testid="stFooter"] {visibility: hidden;}
    #MainMenu {visibility: hidden;}

    /* Tipografia Limpa e Global */
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    /* Fundo da área principal (Off-white no tema claro, chumbo no escuro) */
    .stApp {
        background-color: var(--background-color);
    }

    /* Remove bordas feias das mensagens de chat */
    [data-testid="stChatMessage"] {
        background-color: transparent !important;
        border: none !important;
        padding: 1.5rem 0 !important;
    }

    /* Avatar minimalista (esconde o ícone padrão feio e deixa só o emoji limpo) */
    [data-testid="chatAvatarIcon-user"] { background-color: transparent !important; }
    [data-testid="chatAvatarIcon-assistant"] { background-color: transparent !important; }

    /* Barra de digitação flutuante e limpa */
    [data-testid="stChatInput"] {
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.2) !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# 2. INICIALIZAÇÃO DO MOTOR IA (RAG LOCAL)
# ==========================================
@st.cache_resource
def iniciar_motor_rag():
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    caminho_db = str(BASE_DIR / "data" / "vector_db")

    # Embedding e VectorStore
    modelo_embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory=caminho_db, embedding_function=modelo_embedding)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4}) 

    # Motor Ollama Local
    llm = ChatOllama(model="llama3", temperature=0)

    # Prompt de Saúde Pública
    prompt_sistema = (
        "Você é o P.U.L.S.E., um assistente de Saúde Pública avançado. "
        "Baseie-se ESTRITAMENTE no contexto fornecido. Se não souber, diga que a informação não consta na base. "
        "Seja direto, técnico e use markdown para formatar listas e negritos.\n\n"
        "Contexto Técnico:\n{context}\n\n"
        "Pergunta: {input}"
    )
    prompt = PromptTemplate(template=prompt_sistema, input_variables=["context", "input"])

    qa_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, qa_chain)

motor_ia = iniciar_motor_rag()


# ==========================================
# 3. ESTRUTURA VISUAL: SIDEBAR E CHAT
# ==========================================

# Gerenciamento de Estado do Histórico
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# --- Barra Lateral (Sidebar) ---
with st.sidebar:
    # Botão de Novo Chat limpo
    if st.button("✏️ Novo Chat", use_container_width=True, type="secondary"):
        st.session_state.mensagens = []
        st.rerun()
    
    st.divider()
    st.markdown("### P.U.L.S.E. Engine")
    st.caption("Modelo: `Llama 3 (Ollama)`")
    st.caption("VectorDB: `ChromaDB`")
    st.caption("Privacidade: `100% Local`")

# --- Área Principal do Chat ---
st.title("P.U.L.S.E.")
st.markdown("<p style='color: gray; font-size: 1.1rem; margin-top: -15px; margin-bottom: 30px;'>Como posso te ajudar com os protocolos de saúde hoje?</p>", unsafe_allow_html=True)

# Renderiza o histórico de mensagens com ícones minimalistas
for msg in st.session_state.mensagens:
    avatar = "👤" if msg["role"] == "user" else "🩺" # Ícone elegante para a IA
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# --- Input do Usuário ---
pergunta_usuario = st.chat_input("Pergunte algo sobre os documentos vetorizados...")

if pergunta_usuario:
    # Exibe pergunta do usuário
    with st.chat_message("user", avatar="👤"):
        st.markdown(pergunta_usuario)
    st.session_state.mensagens.append({"role": "user", "content": pergunta_usuario})

    # Exibe resposta da IA com Spinner limpo
    with st.chat_message("assistant", avatar="🩺"):
        with st.spinner("Analisando contexto..."):
            resposta_completa = motor_ia.invoke({"input": pergunta_usuario})
            texto_resposta = resposta_completa["answer"]
            st.markdown(texto_resposta)
    
    # Salva no histórico
    st.session_state.mensagens.append({"role": "assistant", "content": texto_resposta})