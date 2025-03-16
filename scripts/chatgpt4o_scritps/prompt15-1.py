# Calcular o faturamento total por produto em dólar
revenue_by_product = all_data.groupby("product_name").agg(
    total_revenue_usd=("price_usd", "sum")
).reset_index()

# Ordenar os produtos pelo maior faturamento
top_revenue_products = revenue_by_product.sort_values(by="total_revenue_usd", ascending=False)

# Exibir os produtos com maior faturamento
top_revenue_products
