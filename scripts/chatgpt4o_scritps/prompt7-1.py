# Calcular o ticket médio para cada site
summary_orders_products["average_ticket_usd"] = summary_orders_products["total_orders"].map(
    lambda orders: summary_by_site.loc[summary_by_site["site"] == summary_orders_products["site"][summary_orders_products["total_orders"] == orders].values[0], "total_sales_usd"].values[0] / orders
)

summary_orders_products
