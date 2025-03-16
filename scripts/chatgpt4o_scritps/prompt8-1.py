# Recalcular o ticket médio corretamente usando os dados já extraídos
summary_orders_products["average_ticket_usd"] = summary_orders_products.apply(
    lambda row: summary_by_site.loc[summary_by_site["site"] == row["site"], "total_sales_usd"].values[0] / row["total_orders"],
    axis=1
)

summary_orders_products[["site", "average_ticket_usd"]]
