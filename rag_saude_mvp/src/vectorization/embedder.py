import logging
from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VectorDBManager:
    def __init__(self, db_path: str):
        self.db_path = str(Path(db_path).resolve())
        self.embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.collection_name = "documentos_saude"

    def create_or_update_db(self, chunks: list):
        if not chunks:
            logging.warning("Nenhum chunk recebido para vetorização.")
            return None

        logging.info(f"Iniciando vetorização de {len(chunks)} fragmentos de texto...")
        
        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory=self.db_path,
            collection_name=self.collection_name
        )
        
        logging.info(f"Sucesso! Dados vetorizados e salvos no banco em: {self.db_path}")
        return vectorstore