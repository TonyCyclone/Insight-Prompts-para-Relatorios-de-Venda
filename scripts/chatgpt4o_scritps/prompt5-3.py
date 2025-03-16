# Agrupar por plataforma (site) e produto, somando as vendas em USD
summary_by_site_product = all_data.groupby(["site", "product_sold"]).agg(
    total_sales_usd=("total_sales_usd", "sum")
).reset_index()

# Agrupar por plataforma (site), somando as vendas totais em USD
summary_by_site = all_data.groupby("site").agg(
    total_sales_usd=("total_sales_usd", "sum")
).reset_index()

summary_by_site_product, summary_by_site
