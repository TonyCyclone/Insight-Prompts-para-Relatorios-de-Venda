# Consolidar os dados de todas as plataformas
all_data = pd.concat(dataframes.values(), ignore_index=True)

# Agrupar por país e calcular o total de vendas e quantidade de produtos vendidos
summary = all_data.groupby("delivery_country").agg(
    total_sales=("total_price", "sum"),
    total_quantity=("quantity", "sum")
).reset_index()

# Ordenar pelo total de vendas em ordem decrescente
summary = summary.sort_values(by="total_sales", ascending=False)

summary
