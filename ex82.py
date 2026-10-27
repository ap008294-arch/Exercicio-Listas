valores = []


print("Por favor, introduza 11 valores:")
for i in range(11):
    valor = input(f"Digite o {i+1}º valor: ")
    valores.append(valor)

print("\n--- VALORES INTRODUZIDOS ---")

for i in range(len(valores)):
    print(valores[i])
    
    if i < len(valores) - 1:
        print("----------------")
