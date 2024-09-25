""" Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
    escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. """

def sequencia(num):
    a, b = 0, 1

    if num == a or num == b:
        return True
    
    while b < num:
        a, b = b, a + b
        if b == num:
            return True
        
    return False

num = int(input("Digite um número: "))

if sequencia(num):
    print(f"{num} pertece à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")
