# # Programação com Acesso a Banco de Dados
# Revisão de Orientação a Objetos
# Prof. Guilherme Leal Santos

#Lista de palavras
frutas = ['Maçã', 'Banana', 'Laranja']
print(frutas)
print(frutas[0])
print(f'Tamanho: {len(frutas)}')

frutas.append('Uva') #adiciona no final
print(frutas)

frutas.insert(1, 'Abacaxi') #escolhe a posição ao adicionar
print(frutas)

# fruta = frutas.pop() -> remove o último elemento da lista
fruta = frutas.pop(0) # -> remove o elemento especificado
print(f'Removido: {fruta}')
print(frutas)

frutas.remove('Uva') #remove um elemento pelo nome
print(frutas)

#Lista de Números
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(numeros)

numeros_ord_c = sorted(numeros)
print(f'Listan ordenada (c):{numeros_ord_c}')
numeros_ord_d = sorted(numeros, reverse=True)
print(f'Listan ordenada (d):{numeros_ord_d}')

#Dobrar números da lista
numeros_dobro = []
for n in numeros:
    numeros_dobro.append(n*2)
print(numeros_dobro)

numeros_dobro = list(map(lambda n: n*2, numeros))
print(numeros_dobro)

#Filtrar números da lista
numeros_filtrados = []
for n in numeros:
    if n > 4:
        numeros_filtrados.append(n)
print(numeros_filtrados)

numeros_filtro = list(filter(lambda n: n>4,numeros))
print(numeros_filtro)

#Reduz a lista a um único valor (soma)
from functools import reduce
soma = reduce(lambda soma, n: soma + n, numeros)
print(soma)
