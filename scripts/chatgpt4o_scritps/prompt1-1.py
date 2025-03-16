import pandas as pd

# Caminhos dos arquivos
files = {
    "Etsy": "/mnt/data/Meganium_Sales_Data_-_Etsy.csv",
    "Shopee": "/mnt/data/Meganium_Sales_Data_-_Shopee.csv",
    "AliExpress": "/mnt/data/Meganium_Sales_Data_-_AliExpress.csv",
}

# Carregar os dados
dataframes = {platform: pd.read_csv(path) for platform, path in files.items()}

# Verificar as primeiras linhas de cada dataset
{platform: df.head() for platform, df in dataframes.items()}
