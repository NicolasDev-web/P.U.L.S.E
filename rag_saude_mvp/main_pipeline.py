from pathlib import Path
from src.ingestion.pdf_extractor import HealthPDFExtractor
from src.processing.chunker import TextChunker
from src.vectorization.embedder import VectorDBManager

# 1. Configuração de Caminhos (Automático)
BASE_DIR = Path(__file__).resolve().parent
caminho_raw = BASE_DIR / "data" / "raw"
caminho_processed = BASE_DIR / "data" / "processed"
caminho_db = BASE_DIR / "data" / "vector_db"

extractor = HealthPDFExtractor(raw_path=caminho_raw, processed_path=caminho_processed)
chunker = TextChunker(chunk_size=1000, chunk_overlap=200)
db_manager = VectorDBManager(db_path=caminho_db)

nome_do_arquivo = "relatorio_pcdt_ist.pdf" #

print("-" * 50)
print(f"🚀 Iniciando o P.U.L.S.E. Pipeline para: {nome_do_arquivo}")

caminho_texto = extractor.extract_text_from_pdf(nome_do_arquivo)

if caminho_texto:
    print("\n🔪 Segmentando o documento...")
    chunks_do_documento = chunker.process_text_file(caminho_texto)
    print(f"Foram gerados {len(chunks_do_documento)} blocos de texto.")

    print("\n🧠 Transformando texto em vetores e salvando no ChromaDB...")
    banco_vetorial = db_manager.create_or_update_db(chunks_do_documento)
    
    print("-" * 50)
    print("✅ Pipeline executado com sucesso! A base de conhecimento está pronta.")
else:
    print("❌ Falha na extração. O pipeline foi interrompido.")