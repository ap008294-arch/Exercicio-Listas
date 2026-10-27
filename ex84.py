pares = []
impares = []

print("Por favor, introduza 12 números inteiros:")
for i in range(12):
    while True:
        try:
            num = int(input(f"Digite o {i+1}º número inteiro: "))
            
            
            if num % 2 == 0:
                pares.append(num)
            else:
                impares.append(num)
                
            break  
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro válido.")

print("\n--- NÚMEROS PARES ---")
if pares:
    for num in pares:
        print(num)
else:
    print("Nenhum número par foi introduzido.")

print("\n--- NÚMEROS ÍMPARES ---")
if impares:
    for num in impares:
        print(num)
else:
    print("Nenhum número ímpar foi introduzido.")
