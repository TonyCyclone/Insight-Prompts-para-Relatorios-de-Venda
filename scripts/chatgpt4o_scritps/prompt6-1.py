# Agrupar por site e calcular o número total de pedidos e a quantidade total de produtos vendidos
summary_orders_products = all_data.groupby("site").agg(
    total_orders=("buyer_name", "count"),  # Cada linha representa um pedido
    total_products_sold=("quantity", "sum")
).reset_index()

summary_orders_products
