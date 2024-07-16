itens = []

for i in range(3):
    item = input().title()
    if len(item) <= 3:
        item = item.upper()
    itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")
