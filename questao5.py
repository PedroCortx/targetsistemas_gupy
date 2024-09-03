# Entrevista para Estágio em Target Sistemas - Gupy - PEDRO CÔRTES LOUREIRO 31/08/2024#
'''5) Escreva um programa que inverta os caracteres de um string. 

IMPORTANTE: 
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 
b) Evite usar funções prontas, como, por exemplo, reverse; 
'''

estringue = input("\nInsira uma sequência de caracteres: ")
invertido = []
n = 0
i = 0

while i in range(len(estringue)):
    n -= 1
    invertido.append(estringue[n])
    i += 1 

print(*invertido, sep='')