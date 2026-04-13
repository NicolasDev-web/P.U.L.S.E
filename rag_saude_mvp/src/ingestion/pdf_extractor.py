import pdfplumber
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HealthPDFExtractor:
    def __init__(self, raw_path: str, processed_path: str):
        self.raw_path = Path(raw_path)
        self.processed_path = Path(processed_path)
        self.processed_path.mkdir(parents=True, exist_ok=True)

    def extract_text_from_pdf(self, filename: str):
        file_path = self.raw_path / filename
        output_path = self.processed_path / f"{file_path.stem}_extracted.txt"
        
        full_text = []
        
        logging.info(f"Iniciando extração do PDF: {filename}")
        
        try:
            with pdfplumber.open(file_path) as pdf:
                for i, page in enumerate(pdf.pages):
                    page_content = page.extract_text()
                    if page_content:
                        full_text.append(f"--- PÁGINA {i+1} ---\n{page_content}")
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write("\n".join(full_text))
                
            logging.info(f"Extração concluída com sucesso! Arquivo salvo em: {output_path}")
            return output_path
            
        except Exception as e:
            logging.error(f"Erro ao processar o PDF {filename}: {e}")
            return None