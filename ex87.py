X = []
Y = []

print("Por favor, introduza 8 números inteiros para o vetor X:")
for i in range(8):
    while True:
        try:
            num = int(input(f"X[{i}]: "))
            X.append(num)
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro válido.")

print("\nPor favor, introduza 8 números inteiros para o vetor Y:")

for i in range(8):
    while True:
        try:
            num = int(input(f"Y[{i}]: "))
            Y.append(num)
            break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro válido.")

print("\n--- RESULTADO DA MULTIPLICAÇÃO (X * Y) ---")

for i in range(8):
    resultado = X[i] * Y[i]
    print(f"X[{i}] * Y[{i}] -> {X[i]} * {Y[i]} = {resultado}")