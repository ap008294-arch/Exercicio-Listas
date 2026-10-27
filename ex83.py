numeros = []

print("Por favor, introduza 18 números inteiros:")
for i in range(18):
    while True:
        try:
            num = int(input(f"Digite o {i+1}º número inteiro: "))
            numeros.append(num)
            break  
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro válido.")

print("\n--- NÚMEROS NA ORDEM INVERSA ---")

for num in numeros[::-1]:
    print(num)
