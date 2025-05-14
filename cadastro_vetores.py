# Um programa que faz um simples cadastro usando vetores
# Desenvolvido por Kauan

# Inicializamos listas para definir a quantidade de cadastros.
nome = [''] * 3
idade = [0] * 3
telefone = [''] * 3
email = [''] * 3
endereco = [''] * 3

contador = 0  # Usado para contar as listas

for contador in range(3):
    print("CADASTRO SIMPLIFICADO")
    print("----------------------")
    print(f"{contador + 1}º Usuário: ")

    nome[contador] = input("Digite o seu nome: ")
    idade[contador] = int(input("Digite a sua idade: "))
    telefone[contador] = input("Digite o seu telefone: ")
    email[contador] = input("Digite o seu email: ")
    endereco[contador] = input("Digite o seu endereço: ")
    print()

# Exibição dos dados cadastrados
print("----------------------")
for contador in range(3):
    print(f"{contador + 1}º Usuário: ")
    print(f"NOME: {nome[contador]}")
    print(f"IDADE: {idade[contador]} anos")
    print(f"TELEFONE: {telefone[contador]}")
    print(f"EMAIL: {email[contador]}")
    print(f"ENDEREÇO: {endereco[contador]}")
    print('---------------------------')
