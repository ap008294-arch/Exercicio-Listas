maiores_de_idade = []

print("Por favor, introduza os dados de 7 pessoas:")


for i in range(7):
    print(f"\n--- {i+1}ª Pessoa ---")
    nome = input("Nome: ").strip()
    
    
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro para a idade.")
    
    
    if idade >= 18:
        maiores_de_idade.append(nome)


print("\n--- PESSOAS COM 18 ANOS OU MAIS ---")
if maiores_de_idade:
    for nome in maiores_de_idade:
        print(nome)
else:
    print("Nenhuma das pessoas listadas tem 18 anos ou mais.")