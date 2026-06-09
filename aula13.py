#Aula 13
'''1. Contador de Vogais - Contar vogais em uma palavra usando FOR'''
palavra = input("Digite uma palavra: ")
contador_vogais = 0
for letra in palavra:
    if letra.lower() in "aeiou":
        contador_vogais += 1
print(f"A palavra '{palavra}' tem {contador_vogais} vogais.")
 
'''2. Tabuada Interativa - Gerar tabuada de um número usando FOR'''
numero = int(input("Digite um número para gerar a tabuada: "))
print(f"Tabuada de {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

'''3. Senha com Tentativas - Validar senha com limite de tentativas usando WHILE'''
senha_correta = "claudia123"
tentativas = 0
while tentativas < 3:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Senha correta! Bem vindo(a).")
        break
    else:
        tentativas += 1
        print(f"Senha incorreta! Tentativas restantes: {3 - tentativas}")
if tentativas == 3:
    print("Número máximo de tentativas atingido. Acesso negado.")
    
'''4. Soma de Pares - Somar números pares de 1 a 100 usando FOR'''
soma_pares = 0
for i in range(1, 101):
    if i % 2 == 0:
        soma_pares += i
print(f"A soma dos números pares de 1 a 100 é: {soma_pares}")

'''5. Adivinhação - Jogo de adivinhar número com dicas usando WHILE'''

'''6. Fibonacci - Gerar sequência de Fibonacci usando WHILE'''
n = int(input("Digite quantos termos da sequência de Fibonacci deseja gerar: "))
a, b = 0, 1
contador = 0
while contador < n:
    print(a, end=' ')
    a, b = b, a + b
    contador += 1
    
'''7. Lista de Compras - Criar lista dinâmica com WHILE e exibir com FOR'''
lista_compras = []
while True:
    item = input("Digite um item para a lista de compras (ou 'sair' para finalizar): ")
    if item.lower() == 'sair':
        break
    lista_compras.append(item)
print("Lista de Compras:")
for item in lista_compras:
    print(f"- {item}")
    
'''8. Verificador de Primo - Verificar se número é primo usando FOR'''
numero = int(input("Digite um número para verificar se é primo: "))
is_prime = True
for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
        is_prime = False
        break
if is_prime and numero > 1:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")

'''9. Calculadora Simples - Calculadora com menu interativo usando WHILE'''
while True:
    print("Calculadora Simples")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    escolha = input("Escolha uma operação: ")
    
    if escolha == '5':
        print("Encerrando a calculadora. Até mais!")
        break
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if escolha == '1':
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif escolha == '2':
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif escolha == '3':
        resultado = num1 * num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif escolha == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Opção inválida. Por favor, escolha uma operação válida.")
'''Exercícios 11-25'''
'''11. Contagem Regressiva com FOR - Contagem regressiva 10 até 1'''
for i in range(10, 0, -1):
    print(i)
    

'''12. Média com WHILE - Calcular média de números até digitar 0'''
soma = 0
contador = 0
while True:
    numero = float(input("Digite um número (ou 0 para finalizar): "))
    if numero == 0:
        break
    soma += numero
    contador += 1
if contador > 0:
    media = soma / contador
    print(f"A média dos números digitados é: {media}")
    

'''13. Tabuada com WHILE - Gerar tabuada usando WHILE em vez de FOR'''
numero = int(input("Digite um número para gerar a tabuada: "))
print(f"Tabuada de {numero}:")
contador = 1
while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1
    
'''14. Fatorial com FOR - Calcular fatorial de um número'''
numero = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print(f"O fatorial de {numero} é: {fatorial}")

'''15. Números Ímpares com WHILE - Exibir ímpares de 1 a 20'''
contador = 1
print("Números ímpares de 1 a 20:")
while contador <= 20:
    if contador % 2 != 0:
        print(contador)
    contador += 1
    
'''16. Soma Dígitos com FOR - Somar dígitos individuais de um número'''
numero = input("Digite um número para somar seus dígitos: ")
soma_digitos = 0    
for digito in numero:
    soma_digitos += int(digito)
print(f"A soma dos dígitos de {numero} é: {soma_digitos}")


'''17. Progressão Aritmética - Gerar PA com termo inicial e razão'''
termo_inicial = int(input("Digite o termo inicial da PA: "))
razao = int(input("Digite a razão da PA: "))
print("Progressão Aritmética:")
for i in range(10):
    termo = termo_inicial + i * razao
    print(termo)

'''18. Validador de Email - Validar email contendo "@" e "."'''
email = input("Digite um email para validar: ")
if "@" in email and "." in email:
    print("Email válido.")      
else:
    print("Email inválido.")
    

'''19. Contador de Consoantes - Contar consoantes em um texto'''
texto = input("Digite um texto para contar as consoantes: ")
consoantes = 0
vogais = "aeiouAEIOU"
for char in texto:
    if char.isalpha() and char not in vogais:
        consoantes += 1
print(f"O número de consoantes em '{texto}' é: {consoantes}")


'''20. Jogo da Forca Simplificado - Jogo da forca com palavras'''
palavra_secreta = "palavra"
letras_adivinhadas = []
while True:
    letra = input("Digite uma letra para adivinhar a palavra: ")
    if letra in palavra_secreta:
        letras_adivinhadas.append(letra)
        print("Letra correta!")
    else:
        print("Letra incorreta!")
    palavra_atual = ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra_secreta])
    print(f"Palavra: {palavra_atual}")
    if palavra_atual == palavra_secreta:
        print("Você adivinhou a palavra!")
        break

'''21. Multiplicação Russa - Algoritmo de multiplicação russa'''

'''22. Sequência de Collatz - Gerar sequência matemática famosa'''
numero = int(input("Digite um número para gerar a sequência de Collatz: "))
print("Sequência de Collatz:")
while numero != 1:
    if numero % 2 == 0:
        numero //= 2
    else:
        numero = 3 * numero + 1
    print(numero)

'''23. Palíndromo com FOR - Verificar se palavra é palíndromo'''
palavra = input("Digite uma palavra para verificar se é palíndromo: ")
palavra = palavra.replace(" ", "").lower()  # Remove espaços e converte para min
if palavra == palavra[::-1]:
    print(f"'{palavra}' é um palíndromo.")
else:
    print(f"'{palavra}' não é um palíndromo.")
    

'''24. Banco com WHILE - Sistema bancário simples com saldo'''
saldo = 1000.0
while True:
    print("Bem-vindo ao Banco Simples")
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")
    
    if escolha == '4':
        print("Obrigado por usar o Banco Simples. Até mais!")
        break
    elif escolha == '1':
        print(f"Seu saldo atual é: R${saldo:.2f}")
    elif escolha == '2':
        valor = float(input("Digite o valor para depositar: "))
        if valor > 0:
            saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")
    elif escolha == '3':
        valor = float(input("Digite o valor para sacar: "))
        if 0 < valor <= saldo:
            saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para saque ou saldo insuficiente.")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        
'''25. Contador Inteligente - Somatória com tratamento de erros'''
soma = 0
while True:
    numero = input("Digite um número para somar (ou 'sair' para finalizar): ")
    if numero.lower() == 'sair':
        break
    try:
        soma += float(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número ou 'sair'.")
print(f"A soma total é: {soma}")