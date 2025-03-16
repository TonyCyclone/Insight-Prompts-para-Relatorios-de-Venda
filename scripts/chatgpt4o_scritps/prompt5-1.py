# Agrupar por plataforma e produto, somando as vendas em USD
summary_by_platform_product = all_data.groupby(["platform", "product_sold"]).agg(
    total_sales_usd=("total_sales_usd", "sum")
).reset_index()

# Agrupar por plataforma, somando as vendas totais em USD
summary_by_platform = all_data.groupby("platform").agg(
    total_sales_usd=("total_sales_usd", "sum")
).reset_index()

summary_by_platform_product, summary_by_platform
