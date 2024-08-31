"""

Autor: Gabriel Finger Conte
Data: 31/08/2024

4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP    : R$67.836,43
• RJ    : R$36.678,66
• MG    : R$29.229,88
• ES    : R$27.165,48
• Outros: R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação 
que cada estado teve dentro do valor total mensal da distribuidora.  

"""

# Importa a biblioteca pra lidar com valores reais
from decimal import Decimal

# Verifica se consegue usar o matplotlib
try:
    # Verifica se consegue importar o matplotlib
    import matplotlib.pyplot as plt

    # Função para mostrar a representatividade estadual em um gráfico 
    def print_representatividade_estadual(rep_est):
        estados = rep_est.keys()
        percentual = rep_est.values()
        plt.figure(figsize=(10,10))
        plt.title("Representatividade no Faturamento Mensal por Estado")
        plt.pie(
            x=percentual,
            labels=estados,
            autopct='%1.2f%%')
        plt.show()
except:
    # Função para mostrar a representatividade estadual no terminal
    def print_representatividade_estadual(rep_est):
        print("Representatividade no Faturamento Mensal por Estado\n")
        for estado,percentual in rep_est.items():
            print(f"- {estado}: {percentual:.2f}%")


# Função para calcular a representatividade estadual no faturamento mensal (recebe um dicionário)
def calcula_percentual_representatividade_faturamento_mensal(faturamento_mensal):
    # Calcula o faturamento mensal total
    faturamento_total = sum(faturamento_mensal.values())
    # Dicionário para salvar a representatividade de cada estado
    representatividade_estadual = {}
    # Determina a representatividade de cada estado
    for estado,valor in faturamento_mensal.items():
        percent_estado = (valor / faturamento_total) * 100
        representatividade_estadual[estado] = percent_estado
    # Retorna a repreentatividade de cada estado
    return representatividade_estadual

# Organiza os dados do mês em um dicionário
faturamento_mensal_agosto = {
    "SP": Decimal('67836.43'),
    "RJ": Decimal('36678.66'),
    "MG": Decimal('29229.88'),
    "ES": Decimal('27165.48'),
    "Outros": Decimal('19849.53') 
}

# Determina a representatividade estadual
rep_est_ago = calcula_percentual_representatividade_faturamento_mensal(faturamento_mensal_agosto)
# Apresenta ao usuário a representativida estadual
print_representatividade_estadual(rep_est_ago)

