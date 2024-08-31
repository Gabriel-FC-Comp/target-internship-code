"""

Autor: Gabriel Finger Conte
Data: 31/08/2024

1) Observe o trecho de código abaixo: 
int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?

Vai ser basicamente um somatório de 0 à 13, o que resulta em 91.

"""

indice = 13
soma = 0
k = 0
while k < indice:
    k +=1
    soma += k
print(soma)