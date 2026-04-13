from src.processing.cleaner import HealthDataCleaner
from src.processing.chunker import TextChunker

# 1. Limpeza
cleaner = HealthDataCleaner(raw_path="data/raw", processed_path="data/processed")
df_limpo = cleaner.load_and_clean_csv("dados_pacientes.csv")
df_anonimo = cleaner.anonymize_data(df_limpo)
txt_path = cleaner.dataframe_to_text(df_anonimo, "pacientes_processados")

# 2. Chunking
chunker = TextChunker()
meus_chunks = chunker.process_text_file(txt_path)

# Visualizando o primeiro chunk gerado
print("Exemplo do primeiro chunk pronto para o VectorDB:")
print(meus_chunks[0].page_content)