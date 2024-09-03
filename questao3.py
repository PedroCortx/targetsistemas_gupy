# Entrevista para Estágio em Target Sistemas - Gupy - PEDRO CÔRTES LOUREIRO 31/08/2024#
'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne: 
• O menor valor de faturamento ocorrido em um dia do mês; 
• O maior valor de faturamento ocorrido em um dia do mês; 
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal. 

IMPORTANTE: 
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; 
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média; 
'''

#```python
print("\n ------ATENÇÃO------"
    "\nNÃO HAVIA JSON OU XML DISPONÍVEL NA PLATAFORMA GUPY." 
    "\nFiz um código que gera um arquivo JSON abaixo."
    "\nÉ possível escolher o mês de Fevereiro em anos bissextos."
    "\n#### Pedro Côrtes Loureiro ####")
import json
import random

def dados_faturamento():
    faturamento = {}
    mes31 = ["janeiro", "março", "maio", "julho",
             "agosto", "outubro", "dezembro"]
    mes30 = ["abril", "junho", "setembro", "novembro"]
    fevereiro = "fevereiro"
    fevbis = "fevbis"
    mes = input("\nInforme o mês (exemplo: dezembro): ").rstrip()

    if mes in mes31:
        for dia in range(1, 32): 
            if dia % 7 in (6, 0): 
                continue
            faturamento[f'Dia_{dia}'] = round(random.uniform(0, 50000), 4)
        return faturamento
    elif mes in mes30:
        for dia in range(1, 31): 
            if dia % 7 in (6, 0): 
                continue
            faturamento[f'Dia_{dia}'] = round(random.uniform(0, 50000), 4)
        return faturamento
    elif mes == "fevereiro":
        anobis = input("\nAno bissexto (S/N)?: ")
        anobis = anobis.rstrip().upper()
        if anobis == "S":
            for dia in range(1, 30): 
                if dia % 7 in (6, 0): 
                    continue
                faturamento[f'Dia_{dia}'] = round(random.uniform(0, 50000), 4)
            return faturamento
        else:
            for dia in range(1, 29): 
                if dia % 7 in (6, 0): 
                    continue
                faturamento[f'Dia_{dia}'] = round(random.uniform(0, 50000), 4)
            return faturamento

faturamento = dados_faturamento()
with open('faturamento.json', 'w') as arquivo:
    json.dump(faturamento, arquivo, indent=4)

def analise(dados):
    valores = list(dados.values())

    if not valores:
        return {
            'menor_valor': None,
            'maior_valor': None,
            'dias_acima_media': 0
        }

    menor_valor = min(valores)
    maior_valor = max(valores)

    media_mes = sum(valores) / len(valores)
    dias_acima_media = 0
    for valor in valores:
        if valor > media_mes:
            dias_acima_media += 1

    return {
        'menor_valor': menor_valor,
        'maior_valor': maior_valor,
        'dias_acima_media': dias_acima_media
    }

with open('faturamento.json', 'r') as arquivo:
    dados_carregados = json.load(arquivo)

resultado = analise(dados_carregados)

print(f"Menor valor de faturamento: R$ {resultado['menor_valor']:.2f}".replace(".",","))
print(f"Maior valor de faturamento: R$ {resultado['maior_valor']:.2f}".replace(".",","))
print(f"Número de dias com faturamento acima da média: {resultado['dias_acima_media']}")
#```


