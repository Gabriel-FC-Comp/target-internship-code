"""

Autor: Gabriel Finger Conte
Data: 31/08/2024

2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido 
no código;

* Resultados Obtidos (Considerando um input de 51):
    Insira um número INTEIRO: 51
    51 não pertence à Sequência de Fibonacci!

"""

# Função que determina se um número está incluso na sequência de Fibonacci
def verifica_fibonacci(user_num: int):
    num_anterior2 = 0 # Registro do antecessor do antecessor do número atual da sequência
    num_anterior = 1 # Registro do antecessor do número atual da sequência
    num_fibonacci = -1 # Registro do número atual da sequência

    # Números negativos não fazem parte de Fibonacci
    if(user_num < 0):
        return False
    
    # Verifica o caso singular do zero
    if(user_num == 0):
        return True

    # Calcula os números da sequência até encontrar um número maior ou igual ao desejado
    while num_fibonacci < user_num:
        # Calcula o próximo número
        num_fibonacci = num_anterior + num_anterior2
        # Atualiza o histórico
        num_anterior2, num_anterior = num_anterior, num_fibonacci

    # Retorna se o número faz ou não parte da sequência
    return num_fibonacci == user_num

##########################################################################################

# Variável para o número a ser analisado
user_num = None

try: # Solicita o número desejado ao usuário
    user_num = int(input("Insira um número INTEIRO: "))
    # Verifica se o número faz ou não parte para informar ao usuário
    if(verifica_fibonacci(user_num)):
        print(str(user_num) + " pertence à Sequência de Fibonacci!")
    else:
        print(str(user_num) + " não pertence à Sequência de Fibonacci!")
except: # Informa ao usuário caso não insira um número inteiro
    print("Apenas números INTEIROS pertence à Sequência de Fibonacci!")



