# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...)
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci
# e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

import math

#----------------------------
def perfect_square(x):
    raiz = int(math.sqrt(x))
    return raiz * raiz == x


def verify_fibonacci(n):
    return perfect_square(5 * n * n + 4) or perfect_square(5 * n * n - 4)
#Retorna uma fórmula baseada na fórmula de Binet, que descobre se pertence a Fibonacci
#----------------------------

print("Descubra se um número faz parte da sequência de Fibonacci.\n")
numero_usuario = input("Digite um número positivo: ")

try:
    numero = int(numero_usuario)
    if verify_fibonacci(numero):
        print(f"O número {numero} pertence à Fibonacci!")
    else:
        print(f"O número {numero} não pertence à Fibonacci.")
except ValueError:
    print("Insira um número válido.")

#Arthur Lemos Bendini