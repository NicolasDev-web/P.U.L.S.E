import pandas as pd
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HealthDataCleaner:
    def __init__(self, raw_path: str, processed_path: str):
        self.raw_path = Path(raw_path)
        self.processed_path = Path(processed_path)
        self.processed_path.mkdir(parents=True, exist_ok=True)

    def load_and_clean_csv(self, filename: str) -> pd.DataFrame:
        file_path = self.raw_path / filename
        logging.info(f"Carregando arquivo: {file_path}")
        
        df = pd.read_csv(file_path, sep=';', encoding='utf-8')

        df.columns = df.columns.str.lower().str.replace(' ', '_')

        df.fillna("Não informado", inplace=True)

        return df

    def anonymize_data(self, df: pd.DataFrame) -> pd.DataFrame:
        pii_columns = ['nome', 'cpf', 'cns', 'rg', 'telefone', 'endereco', 'email']
        
        cols_to_drop = [col for col in pii_columns if col in df.columns]
        
        if cols_to_drop:
            df.drop(columns=cols_to_drop, inplace=True)
            logging.info(f"Colunas anonimizadas removidas: {cols_to_drop}")
            
        return df

    def dataframe_to_text(self, df: pd.DataFrame, output_filename: str):
        text_documents = []
        
        for index, row in df.iterrows():
            row_text = ", ".join([f"{col.replace('_', ' ').title()}: {val}" for col, val in row.items()])
            text_documents.append(row_text)

        output_path = self.processed_path / f"{output_filename}.txt"
        with open(output_path, 'w', encoding='utf-8') as f:
            for doc in text_documents:
                f.write(doc + "\n---\n") 
                
        logging.info(f"Dados convertidos para texto salvos em: {output_path}")
        return output_path