# [LPIA-A04] Você está desenvolvendo um programa em Python para calcular a soma dos 
# números pares dentro de um intervalo determinado pelo usuário. O programa deve solicitar 
# ao usuário que insira dois números inteiros, representando o início e o fim do intervalo (inclusive).
# Utilize um loop 'for' para iterar sobre todos os números no intervalo e somar apenas os números pares. 
# Implemente a estrutura 'else' para exibir uma mensagem indicando que não há números pares no intervalo, caso seja o caso.

#Ao final, exiba a soma dos números pares encontrados.

intervalo = int(input("Digite o início do intervalo: "))
intervalo2 = int(input("Digite o fim do intervalo: "))
soma = 0
pares = False

for i in range(intervalo, intervalo2 + 1):
    if i % 2 == 0:
        soma += i
        pares = True

if pares:
    print(f"A soma dos números pares no intervalo é: {soma}")

else:
    print("Não há números pares nesse intervalo.")