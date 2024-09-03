# Entrevista para Estágio em Target Sistemas - Gupy - PEDRO CÔRTES LOUREIRO #
'''1)	Observe o trecho de código abaixo: 
int INDICE = 13, SOMA = 0, K = 0; 
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA); 
Ao final do processamento, qual será o valor da variável SOMA?
'''

#```python
indice = 13
soma = 0
K = 0

while K < indice:
    K += 1
    soma += K
    #print(K, soma) #teste

print("O valor da variável soma é: ", soma)
#```