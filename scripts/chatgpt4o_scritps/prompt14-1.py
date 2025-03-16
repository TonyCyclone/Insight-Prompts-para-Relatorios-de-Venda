# Definir as estações do ano para cada país (considerando hemisférios)
seasons = {
    "Japan": {  # Hemisfério Norte
        "Spring": ("03-01", "05-31"),
        "Summer": ("06-01", "08-31"),
        "Autumn": ("09-01", "11-30"),
        "Winter": ("12-01", "02-28"),
    },
    "Germany": {  # Hemisfério Norte
        "Spring": ("03-01", "05-31"),
        "Summer": ("06-01", "08-31"),
        "Autumn": ("09-01", "11-30"),
        "Winter": ("12-01", "02-28"),
    },
    "Australia": {  # Hemisfério Sul
        "Spring": ("09-01", "11-30"),
        "Summer": ("12-01", "02-28"),
        "Autumn": ("03-01", "05-31"),
        "Winter": ("06-01", "08-31"),
    },
    "Canada": {  # Hemisfério Norte
        "Spring": ("03-01", "05-31"),
        "Summer": ("06-01", "08-31"),
        "Autumn": ("09-01", "11-30"),
        "Winter": ("12-01", "02-28"),
    },
    "France": {  # Hemisfério Norte
        "Spring": ("03-01", "05-31"),
        "Summer": ("06-01", "08-31"),
        "Autumn": ("09-01", "11-30"),
        "Winter": ("12-01", "02-28"),
    },
    "United Kingdom": {  # Hemisfério Norte
        "Spring": ("03-01", "05-31"),
        "Summer": ("06-01", "08-31"),
        "Autumn": ("09-01", "11-30"),
        "Winter": ("12-01", "02-28"),
    },
    "United States": {  # Hemisfério Norte
        "Spring": ("03-01", "05-31"),
        "Summer": ("06-01", "08-31"),
        "Autumn": ("09-01", "11-30"),
        "Winter": ("12-01", "02-28"),
    },
}

# Função para atribuir estação do ano com base na data e país
def get_season(date, country):
    month_day = date.strftime("%m-%d")
    for season, (start, end) in seasons.get(country, {}).items():
        if start <= month_day <= end:
            return season
    return "Unknown"

# Aplicar a função de estação ao dataset
all_data["season"] = all_data.apply(lambda row: get_season(row["date"], row["country"]), axis=1)

# Agrupar os dados por país e estação para encontrar picos de pedidos e produtos vendidos
seasonal_sales = all_data.groupby(["country", "season"]).agg(
    total_orders=("buyer_name", "count"),
    total_products_sold=("quantity", "sum")
).reset_index()

# Identificar a estação com maior número de pedidos e produtos vendidos para cada país
peak_seasons = seasonal_sales.loc[seasonal_sales.groupby("country")["total_orders"].idxmax()][["country", "season", "total_orders"]]
peak_products = seasonal_sales.loc[seasonal_sales.groupby("country")["total_products_sold"].idxmax()][["country", "season", "total_products_sold"]]

# Exibir os resultados
peak_seasons, peak_products
