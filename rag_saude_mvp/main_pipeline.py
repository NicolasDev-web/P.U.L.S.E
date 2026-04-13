from pathlib import Path
from src.ingestion.pdf_extractor import HealthPDFExtractor

BASE_DIR = Path(__file__).resolve().parent

caminho_raw = BASE_DIR / "data" / "raw"
caminho_processed = BASE_DIR / "data" / "processed"

extractor = HealthPDFExtractor(raw_path=caminho_raw, processed_path=caminho_processed)

nome_do_arquivo = "relatorio_pcdt_ist.pdf" 

print(f"Iniciando a leitura do {nome_do_arquivo}...")
caminho_resultado = extractor.extract_text_from_pdf(nome_do_arquivo)

if caminho_resultado:
    print(f"Sucesso absoluto! O texto foi extraído e salvo em: {caminho_resultado}")
else:
    print("Ops, algo deu errado na extração.")