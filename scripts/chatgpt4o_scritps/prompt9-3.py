# Converter a coluna de data correta para datetime
all_data["date"] = pd.to_datetime(all_data["date"], errors="coerce")

# Agrupar por data e calcular o número de pedidos e quantidade de produtos vendidos
sales_over_time = all_data.groupby("date").agg(
    total_orders=("buyer_name", "count"),
    total_products_sold=("quantity", "sum")
).reset_index()

# Criar o gráfico de vendas ao longo do tempo
plt.figure(figsize=(12, 6))
plt.plot(sales_over_time["date"], sales_over_time["total_orders"], marker="o", linestyle="-", label="Total de Pedidos")
plt.plot(sales_over_time["date"], sales_over_time["total_products_sold"], marker="s", linestyle="--", label="Total de Produtos Vendidos")

# Configurações do gráfico
plt.xlabel("Data do Pedido")
plt.ylabel("Quantidade")
plt.title("Quantidade de Vendas ao Longo do Tempo")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Mostrar gráfico
plt.show()

# Exibir a tabela de vendas ao longo do tempo
sales_over_time
