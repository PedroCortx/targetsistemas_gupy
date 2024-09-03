# Entrevista para Estágio em Target Sistemas - Gupy - PEDRO CÔRTES LOUREIRO 31/08/2024#
'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado: 
•	SP - R$67.836,43 
•	RJ - R$36.678,66 
•	MG - R$29.229,88 
•	ES - R$27.165,48 
•	Outros - R$19.849,53 

Escreva um programa na linguagem que desejar onde calcule o percentual 
de representação que cada estado teve dentro do valor total mensal da distribuidora. 
'''

#```python
faturamento_mensal = {"SP"    : 67836.43,
                      "RJ"    : 36678.66,
                      "MG"    : 29229.88,
                      "ES"    : 27165.48,
                      "Outros": 19849.53}
percentuais = { "SP"    : 0,
                "RJ"    : 0,
                "MG"    : 0,
                "ES"    : 0,
                "Outros": 0}

total_mensal = round(sum(_ for _ in faturamento_mensal.values()), 2)

for chave in faturamento_mensal.keys():
    percentuais[chave] = faturamento_mensal[chave] / (total_mensal / 100)
    percentuais[chave] = str(round(percentuais[chave], 2))
    percentuais[chave] = percentuais[chave].replace('.', ',')

print(f"\nO faturamento total mensal foi de: R$ {total_mensal}".replace('.',','))
print("\nO percentual de cada Estado no faturamento total mensal:")
print(*percentuais.items(), sep="\n")
#```