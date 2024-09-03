# Entrevista para Estágio em Target Sistemas - Gupy - PEDRO CÔRTES LOUREIRO 31/08/2024#
'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o 
próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando 
se o número informado pertence ou não a sequência. 
IMPORTANTE: Esse número pode ser informado através de qualquer entrada 
de sua preferência ou pode ser previamente definido no código; 
'''
#```python
nacci = 0
fibo1 = 0
fibo2 = 1
fibonacci = []

try:
    numero = int(input("\nInforme um número inteiro positivo: "))
    if numero < 0:
        print("Número inválido. Reinicie o programa.")
    else:  
        while nacci <= numero:
            fibonacci.append(nacci)
            nacci = fibo1 + fibo2
            fibo2 = fibo1
            fibo1 = nacci
        #print(f"A sequência de Fibonacci até seu número: ({fibonacci})", fibo1, fibo2, nacci) # teste
        if numero in fibonacci:
            print(f"\nSeu número, {numero}, faz parte da sequência de Fibonacci.")
        else:
            print(f"\nSeu número, {numero}, não faz parte da sequência de Fibonacci.")
        print("A sequência de Fibonacci até seu número:")
        print(*fibonacci, sep=",")
except:
    print("Não foi possível executar o programa. Reinicie e tente novamente.")
#```