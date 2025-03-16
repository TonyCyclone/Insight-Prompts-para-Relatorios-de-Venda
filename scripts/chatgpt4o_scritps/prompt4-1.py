from datetime import datetime

# Converter a coluna de data de nascimento para o formato datetime
all_data["buyer_birth_date"] = pd.to_datetime(all_data["buyer_birth_date"], errors="coerce")

# Calcular a idade dos compradores
current_year = datetime.now().year
all_data["buyer_age"] = current_year - all_data["buyer_birth_date"].dt.year

# Agrupar por país e produto, calculando a idade média, quantidade de compradores e quantidade de vendas
summary_by_product = all_data.groupby(["delivery_country", "product_sold"]).agg(
    avg_buyer_age=("buyer_age", "mean"),
    total_buyers=("buyer_name", "count"),  # Cada linha representa uma compra de um comprador
    total_sales_usd=("total_sales_usd", "sum"),
    total_quantity=("quantity", "sum")
).reset_index()

# Ordenar pelo total de vendas em USD
summary_by_product = summary_by_product.sort_values(by=["delivery_country", "total_sales_usd"], ascending=[True, False])

summary_by_product
