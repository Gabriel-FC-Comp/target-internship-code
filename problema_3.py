"""

Autor: Gabriel Finger Conte
Data: 31/08/2024
OBS: Dados do arquivo .json são fictícios, tendo sido gerados com o Microsoft Copilot 

3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na 
linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


"""

import json
from decimal import Decimal

# Função para importar os dados do faturamento.json
def importa_faturamento_json(path_arq: str):
    info_faturamento = None
    with open(path_arq,"r") as faturamento_json:
        info_faturamento = json.load(faturamento_json)
    return info_faturamento

# Função para tratamento dos dados
def mapeamento_decimal(faturamento_mensal):
    for notacao_diaria in faturamento_mensal:
        # Pega as strings para converter em Decimal
        string_valores = list(map(str,notacao_diaria['valores']))
        notacao_diaria['valores'] = list(map(Decimal,string_valores))
    return faturamento_mensal

# Função para analisar o faturamento (recebe um vetor de dicionários)
def analisa_faturamento(faturamento_mensal):

    # Dicionário para salvar as informações desejadas
    parametros_analisados = {
        "menor_faturamento": float('inf'),
        "maior_faturamento": float('-inf'),
        "dias_fat_superior": 0
    }

    # Vetor auxiliar para armazenar os faturamentos diários
    faturamentos_diarios = []
    
    # Variáveis auxiliares pro cálculo da média mensal
    soma_mensal = Decimal('0')
    dias_quantificaveis = Decimal('0')

    # Percorre cada registro diário
    for notacao_diaria in faturamento_mensal:
        # Verifica se houve faturamento no dia
        if(not len(notacao_diaria['valores']) == 1 or not notacao_diaria['valores'][0] == 0):
            # Calcula o faturamento diário
            fat_diario = sum(notacao_diaria['valores'])
            
            # Salva o faturamento diário calculado
            faturamentos_diarios.append(fat_diario)
            
            # Atualiza o menor faturamento pontual
            parametros_analisados['menor_faturamento'] = min(min(notacao_diaria['valores']),parametros_analisados['menor_faturamento'])
            # Atualiza o maior faturamento pontual
            parametros_analisados['maior_faturamento'] = max(max(notacao_diaria['valores']),parametros_analisados['maior_faturamento'])
            # Adiciona o faturamento diário para o cálculo do total mensal
            soma_mensal += fat_diario
            dias_quantificaveis += 1

    # Obtém o valor da média mensal
    media_mensal = (soma_mensal / dias_quantificaveis)

    # Percorre os faturamentos diários para analise dos dias que ultrapassaram a média mensal
    for fat_diario in faturamentos_diarios:
        if(fat_diario > media_mensal):
            parametros_analisados['dias_fat_superior'] += 1

    # Retorna os parâmetros solicitados
    return parametros_analisados



##########################################################

"""
    Ex de formato json esperado:

    {
        "mes_referencia": "agosto",
        "faturamento": [
            {
                "dia": 1,
                "valores": [
                    1000.0,
                    1500.0,
                    2000.0
                ]
            },
            ...
        ],
    }
"""
# Caminho pro arquivo .json
path_arq = "faturamento_mensal.json" 
# Importa os dados do JSON
info_faturamento = importa_faturamento_json(path_arq)
# Mapeia os dados pra Decimal, evitando problemas de casas decimais
faturamento_mensal = mapeamento_decimal(info_faturamento['faturamento'])
# Analisa os parâmetros solicitados
parametros_analisados = analisa_faturamento(faturamento_mensal)
# Informa os parâmetros no terminal
print("\nDados do Faturamento de " + info_faturamento['mes_referencia'] + ":")
for info,valor in parametros_analisados.items():
    print("- " + info + ": " + str(valor))

