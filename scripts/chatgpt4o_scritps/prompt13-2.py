# Converter a coluna de data para datetime
all_data["date"] = pd.to_datetime(all_data["date"], errors="coerce")

# Renomear a coluna de país para padronização
all_data.rename(columns={"delivery_country": "country"}, inplace=True)

# Filtrar os dados apenas para o Japão
japan_sales = all_data[all_data["country"] == "Japan"].copy()

# Definir as datas dos feriados no Japão
japan_holidays = {
    "Dia da Montanha": "2024-08-12",
    "Dia do Idoso": "2024-09-16",
    "Dia do Esporte": "2024-10-14"
}

# Converter as datas para datetime para facilitar a análise
japan_holidays = {k: pd.to_datetime(v) for k, v in japan_holidays.items()}

# Criar um dicionário para armazenar as vendas nos períodos analisados
holiday_sales_analysis = {}

# Analisar as vendas 7 dias antes e 7 dias depois de cada feriado
for holiday_name, holiday_date in japan_holidays.items():
    # Definir o intervalo de análise
    start_date = holiday_date - pd.Timedelta(days=7)
    end_date = holiday_date + pd.Timedelta(days=7)

    # Filtrar as vendas nesse período
    period_sales = japan_sales[(japan_sales["date"] >= start_date) & (japan_sales["date"] <= end_date)]

    # Agrupar por data e contar o número de pedidos e produtos vendidos
    period_summary = period_sales.groupby("date").agg(
        total_orders=("buyer_name", "count"),
        total_products_sold=("quantity", "sum")
    ).reset_index()

    # Armazenar os resultados
    holiday_sales_analysis[holiday_name] = period_summary

# Exibir os resultados
holiday_sales_analysis
