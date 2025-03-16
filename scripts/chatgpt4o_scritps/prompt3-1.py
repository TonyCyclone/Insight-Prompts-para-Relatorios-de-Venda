# Taxa de conversão de USD para BRL (aproximada)
usd_to_brl = 5.00  # 1 USD ≈ 5 BRL

# Somatório das vendas em USD
total_sales_usd = summary_usd["total_sales_usd"].sum()

# Converter para BRL
total_sales_brl = total_sales_usd * usd_to_brl

total_sales_usd, total_sales_brl
