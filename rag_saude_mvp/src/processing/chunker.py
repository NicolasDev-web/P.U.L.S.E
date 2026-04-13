from langchain_text_splitters import RecursiveCharacterTextSplitter
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TextChunker:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )

    def process_text_file(self, file_path: str):
        logging.info(f"Iniciando chunking do arquivo: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            full_text = f.read()

        raw_documents = full_text.split("\n---\n")
        
        chunks = self.splitter.create_documents(raw_documents)
        
        logging.info(f"Arquivo dividido em {len(chunks)} chunks semânticos.")
        return chunks