import pandas as pd

# Caminhos dos arquivos
file_paths = {
    "Etsy": "/mnt/data/Meganium_Sales_Data_-_Etsy.csv",
    "Shopee": "/mnt/data/Meganium_Sales_Data_-_Shopee.csv",
    "AliExpress": "/mnt/data/Meganium_Sales_Data_-_AliExpress.csv",
}

# Carregar os arquivos CSV
dataframes = {site: pd.read_csv(path) for site, path in file_paths.items()}

# Adicionar a informação da plataforma de origem em cada DataFrame
for site, df in dataframes.items():
    df["site"] = site

# Unir os dados em um único DataFrame
all_data = pd.concat(dataframes.values(), ignore_index=True)

# Verificar colunas para identificar quais precisam ser renomeadas ou ajustadas
all_data.head()
