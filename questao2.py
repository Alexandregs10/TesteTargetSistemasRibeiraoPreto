# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def input_palavra():
    text = input("Insira uma palavra: \n")
    if text.islower():
        print("A palavra é minúscula.")
    elif text.isupper():
        print("A palavra é maiúscula.")
    else:
        print("A palavra contém uma mistura de maiúsculas e minúsculas.")

def contador_palavra(text):
    letra = input("Insira a letra que deseja contar: \n")
    contador = text.lower().count(letra.lower())
    print(f"A letra '{letra}' aparece {contador} vezes na palavra '{text}'.")

while True:
    print("\nMenu:")
    print("1. Verificar se a palavra é minúscula ou maiúscula")
    print("2. Contar quantas vezes uma letra aparece na palavra")
    print("3. Sair")
    
    escolha = input("Escolha uma opção (1/2/3): \n")
    
    if escolha == "1":
        input_palavra()
    elif escolha == "2":
        text = input("Insira uma palavra para análise: \n")
        contador_palavra(text)
    elif escolha == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida, tente novamente.")
