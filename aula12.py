# Aula 12 
'''1. Adicionar elementos a uma lista 
Crie uma lista vazia e adicione 5 números inteiros a ela usando o método `append()`. 
Em seguida, imprima a lista.'''

lista = []
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
print(lista)

'''Remover elementos de uma lista 
Crie uma lista com 5 strings e remova o segundo elemento da lista usando o método 
`pop()`. Em seguida, imprima a lista. '''

frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]
frutas.pop(1)
print(frutas)

'''3. Ordenar uma lista: 
Crie uma lista com 5 números inteiros e ordene-a em ordem crescente usando o 
método `sort()`. Em seguida, imprima a lista. '''

numeros = [5, 2, 9, 1, 3]
numeros.sort()
print(numeros)

'''4. Acessar elementos de uma tupla: 
Crie uma tupla com 5 strings e acesse o terceiro elemento da tupla usando o índice. 
Em seguida, imprima o elemento. '''

cores = ("vermelho", "azul", "verde", "amarelo", "roxo")
print(cores[2])


'''Crie duas tuplas com 3 números inteiros cada e concatene-as usando o operador `+`. 
Em seguida, imprima a tupla resultante. '''

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)

'''6.Lista de frutas: 
Crie uma lista com 5 frutas diferentes e imprima a lista. Em seguida, adicione uma 
nova fruta à lista e imprima a lista novamente. '''

frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]
print(frutas)
frutas.append("manga")
print(frutas)  

'''7.Lista de nomes: 
Crie uma lista com 5 nomes de pessoas e imprima a lista. Em seguida, remova o 
último nome da lista e imprima a lista novamente. '''

nomes = ["Alice", "Bob", "Charlie", "David", "Eve"] 
print(nomes)
nomes.pop()
print(nomes)

'''8.Lista de números: 
Crie uma lista com 5 números racionais/fracionários e ordene-a em ordem crescente. 
Em seguida, imprima a lista ordenada. '''

numeros = [3.5, 1.2, 4.8, 2.1, 5.0]
numeros.sort()
print(numeros)

''''9.Tupla de frutas: 
Crie uma tupla com 3 frutas diferentes e imprima a tupla. Em seguida, acesse o 
segundo elemento da tupla e imprima-o. '''

frutas = ("maçã", "banana", "laranja")
print(frutas)
print(frutas[1])

'''10 .Tupla de nomes: 
Crie uma tupla com 2 nomes de pessoas e concatene-a com outra tupla que contenha 
2 nomes de pessoas. Em seguida, imprima a tupla resultante.'''

tupla1 = ("Alice", "Bob")
tupla2 = ("Junior", "David")
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)

'''11:Crie uma string com 5 letras e converta-a para uma lista usando a função list(). Em 
seguida, imprima a lista. '''
string = "Olá"
lista = list(string)
print(lista)

'''12.Crie uma tupla com 3 números inteiros e converta-a para uma lista usando a função 
list() Em seguida, imprima a lista. '''
tupla = (1, 2, 3)
lista = list(tupla)
print(lista)

'''13:Crie um conjunto (set) com 5 números inteiros e converta-o para uma lista usando 
a função list(. Em seguida, imprima a lista. '''
conjunto = {1, 2, 3, 4, 5}
lista = list(conjunto)
print(lista)

'''14.Qual a diferença de uma lista e um conjunto (set)'''
 
 
