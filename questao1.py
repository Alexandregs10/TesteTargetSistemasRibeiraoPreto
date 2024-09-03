# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


value = int(input("Digite um número para verificar se pertence à sequência de Fibonacci:\n"))

def pertence_fibonacci(num):
    num1 = 0
    num2 = 1
    next_number = num2
    
    print("Sequência de Fibonacci abaixo até o seu número: ")
    
    while next_number <= num:
        print(next_number, end=' ')
        
        if next_number == num:
            return True
        num1, num2 = num2, next_number
        next_number = num1 + num2
    return False

if pertence_fibonacci(value):
    print(f"\nO número {value} pertence à sequência de Fibonacci.")
else:
    print(f"\nO número {value} NÃO pertence à sequência de Fibonacci.")
