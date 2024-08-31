"""

Autor: Gabriel Finger Conte
Data: 31/08/2024

5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

* Resultados Obtidos:
    Digite uma string para inverter: Target Sistemas
    A string invertida fica: sametsiS tegraT

"""

# Função para inverter os caracteres de uma string
def inverte_string(string_alvo):
    string_invertida = ""
    # Percorre a string de trás para frente, salvando cada caractere
    for i in range(len(string_alvo)-1, -1, -1):
        string_invertida += string_alvo[i]
    # Retorna a string com os caracteres invertidos
    return string_invertida

######################################################################

# Pede uma string pro usuário
string_alvo = input("Digite uma string para inverter: ")
# Inverte a string
string_invertida = inverte_string(string_alvo)
# Informa ao usuário
print("A string invertida fica: " + string_invertida)