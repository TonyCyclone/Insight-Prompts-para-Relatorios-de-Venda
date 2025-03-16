# Verificar os nomes das colunas em cada dataset
column_names = {platform: df.columns.tolist() for platform, df in dataframes.items()}
column_names
