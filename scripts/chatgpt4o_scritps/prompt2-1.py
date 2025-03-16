# Taxas de conversão para USD
exchange_rates = {"EUR": 1.10, "GBP": 1.25, "USD": 1.00}

# Converter todas as vendas para USD
all_data["total_sales_usd"] = all_data.apply(
    lambda row: row["total_price"] * exchange_rates.get(row["currency"], 1.00), axis=1
)

# Agrupar por país e calcular o total de vendas em USD e quantidade total de produtos vendidos
summary_usd = all_data.groupby("delivery_country").agg(
    total_sales_usd=("total_sales_usd", "sum"),
    total_quantity=("quantity", "sum")
).reset_index()

# Ordenar pelo total de vendas em ordem decrescente
summary_usd = summary_usd.sort_values(by="total_sales_usd", ascending=False)

summary_usd
