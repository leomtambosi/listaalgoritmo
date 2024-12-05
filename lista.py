# STRINGS

# ctrl + k + u para descomentar o cógigo desejado
# CTRL + K + C para comentar novamente

# exercicio 1

# nome = input("Digite o seu nome: ")
# invertido = ""

# for i in range(len(nome) - 1, -1, -1):
#     invertido += nome[i]

# nomeInvertido = invertido.upper()

# print(f"O seu nome invertido é: {nomeInvertido}")



# exercicio 2

# frase = input("Digite uma frase: ")

# espacos = 0
# vogais = {'a', 'e', 'i', 'o', 'u'}
# contagem = 0

# for char in frase:
#     if char == ' ':
#         espacos += 1
#     elif char.lower() in vogais:
#         contagem += 1

# print(f"Quantidade de espaços em branco: {espacos}")
# print(f"Quantidade de vogais: {contagem}")



# EXERCICIO 3

# codigo = input("Digite um código de 5 algarismos: ")

# if len(codigo) == 5 and codigo.isdigit():
#     A = int(codigo[0])
#     B = int(codigo[1])
#     C = int(codigo[2])
#     D = int(codigo[3])
#     E = int(codigo[4])

#     S = 6 * A + 5 * B + 4 * C + 3 * D + 2 * E

#     DigitoV = S % 7

#     print(f"O dígito verificador é: {DigitoV}")
# else:
#     print("não é valido")



# EXERCICIO 4

# extenso = {
#     '0': 'zero', '1': 'um', '2': 'dois', '3': 'três', '4': 'quatro',
#     '5': 'cinco', '6': 'seis', '7': 'sete', '8': 'oito', '9': 'nove'
# }

# numero = input("Digite um número: ")

# if numero.isdigit():
#     digitosExtenso = [extenso[digit] for digit in numero]
    
#     print(", ".join(digitosExtenso))
# else:
#     print("Por favor, insira um número válido.")




# EXERCICIO 5

# leet = {
#     'a': '4', 'A': '4','e': '3', 'E': '3','i': '1', 'I': '1','o': '0', 'O': '0','t': '7', 'T': '7','s': '5', 'S': '5','b': '8', 'B': '8'
# }

# def converterleet(texto):
#     textoleet = ''
#     for char in texto:
#         textoleet += leet.get(char, char)
#     return textoleet

# texto = input("Digite um texto: ")

# textoleet = converterleet(texto)

# print("Texto em Leet:", textoleet)




# EXERCICIO 6

# conectores = ['e', 'do', 'da', 'dos', 'das', 'de', 'di', 'du']

# def gerarIniciais(nome):
#     partes = nome.split()
    
#     iniciais = [parte[0].upper() for parte in partes if parte.lower() not in conectores]
    
#     return ''.join(iniciais)

# nome = input("Digite seu nome completo: ")

# iniciais = gerarIniciais(nome)

# print("Iniciais:", iniciais)



# EXERCICIO 7

# def anagramas(str1, str2):
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
    
#     return sorted(str1) == sorted(str2)

# s1 = input("Digite a primeira string: ")
# s2 = input("Digite a segunda string: ")

# if anagramas(s1, s2):
#     print("As strings são anagramas.")
# else:
#     print("As strings não são anagramas.")




# EXERCICIO 8
# frase = input("Digite uma frase: ")

# fraseconvertida = frase.swapcase()

# print("Frase convertida:", fraseconvertida)


# VETORES

# EXERCICIO 1

# A = []

# for i in range(100):
#     valor = float(input(f"Digite o {i+1}º valor: "))
#     A.append(valor)

# soma = sum(A)

# media = soma / len(A)

# maior = max(A)

# menor = min(A)

# print(f"Soma: {soma}")
# print(f"Média: {media}")
# print(f"Maior valor: {maior}")
# print(f"Menor valor: {menor}")



# EXERCICIO 2

# v1 = [10, 20, 30, 40, 50]

# v2 = []

# for i in range(len(v1)):
#     v2.append(v1[i])

# print("V1:", v1)
# print("V2:", v2)



# EXERCICIO 3

# v1 = [102, 2230, 302, 430, 50221] 
# v2 = [321, 432, 343, 443, 125]     

# v3 = []

# for i in range(len(v1)):
#     v3.append(v1[i] + v2[i])

# print("Vetor 1:", v1)
# print("Vetor 2:", v2)
# print("Vetor 3:", v3)




# EXERCICIO 4

# v1 = []
# v2 = []

# print("Digite 15 números para o vetor V1:")
# for i in range(15):
#     v1.append(int(input(f"V1[{i+1}]: ")))

# print("Digite 15 números para o vetor V2:")
# for i in range(15):
#     v2.append(int(input(f"V2[{i+1}]: ")))

# contagem = 0

# for i in range(15):
#     if v1[i] == v2[i]:
#         contagem += 1

# print(f"Quantidade de vezes que V1 e V2 possuem os mesmos números nas mesmas posições: {contagem}")




# EXERCICIO 5

# A = [2, 4, 7, 13, 14, 15, 16]
# B = [1, 6, 7, 11, 13, 16, 18]
# uniao = []

# for item in A:
#     if item not in uniao: 
#         uniao.append(item)

# for item in B:
#     if item not in uniao:
#         uniao.append(item)

# interseccao = []
# for item in A:
#     if item in B and item not in interseccao:
#         interseccao.append(item)

# diferenca = []
# for item in A:
#     if item not in B:
#         diferenca.append(item)

# print("A ⋃ B:", uniao)
# print("A ⋂ B:", interseccao)
# print("A − B:", diferenca)




# EXERCICIO 6

# vetor = []

# print("Digite 20 números:")
# for i in range(20):
#     vetor.append(int(input(f"Elemento {i+1}: ")))

# print("Vetor original:")
# print(vetor)

# for i in range(10):
#     vetor[i], vetor[19-i] = vetor[19-i], vetor[i]

# print("Vetor inverso:")
# print(vetor)




# EXERCICIO 7

# matriculas = []

# for i in range(100):
#     matricula = int(input(f"Digite o número da matrícula {i+1}: "))
    
#     if matricula in matriculas:
#         print("Alerta: Este número de matrícula já foi registrado. Tente novamente.")
#     else:
#         matriculas.append(matricula)

# print("Matrículas cadastradas:")
# print(matriculas)




# EXERCICIO 8

# def main():
#     N = int(input("Digite o número de elementos do vetor: "))

#     vetor = []

#     print(f"Digite {N} números inteiros:")
#     for i in range(N):
#         numero = int(input(f"Elemento {i+1}: "))
#         vetor.append(numero)

#     pares = []
#     impares = []

#     for num in vetor:
#         if num % 2 == 0:
#             pares.append(num)
#         else:
#             impares.append(num)

#     print("Vetor original:", vetor)
#     print("Vetor de números pares:", pares)
#     print("Vetor de números ímpares:", impares)

# main()



# EXERCICIO 9

# def intercalar(vetorA, vetorB):
#     vetorC = []

#     i = j = 0

#     while i < len(vetorA) and j < len(vetorB):
#         if vetorA[i] < vetorB[j]:
#             vetorC.append(vetorA[i])
#             i += 1
#         else:
#             vetorC.append(vetorB[j])
#             j += 1

#     while i < len(vetorA):
#         vetorC.append(vetorA[i])
#         i += 1

#     while j < len(vetorB):
#         vetorC.append(vetorB[j])
#         j += 1

#     return vetorC

# def main():
#     N = int(input("Digite o número de elementos do vetor A: "))
#     vetorA = []
#     print("Digite os elementos do vetor A (já ordenados):")
#     for i in range(N):
#         vetorA.append(int(input(f"Elemento {i+1}: ")))

#     M = int(input("Digite o número de elementos do vetor B: "))
#     vetorB = []
#     print("Digite os elementos do vetor B (já ordenados):")
#     for i in range(M):
#         vetorB.append(int(input(f"Elemento {i+1}: ")))

#     vetorC = intercalar(vetorA, vetorB)

#     print("Vetor C (intercalado e ordenado):")
#     print(vetorC)

# main()




# EXERCICIO 10

# def calcular(notas):
#     notas.sort()

#     notasRestantes = notas[1:-1] 

#     mediaFinal = sum(notasRestantes) / len(notasRestantes)

#     return mediaFinal

# notas = [9.9, 9.7, 9.8, 10, 10]

# media = calcular(notas)
# print(f"A média final é: {media:.2f}")




# EXERCICIO 11

# def somar_sequencias(seq1, seq2):
#     resultado = []
    
#     carry = 0
    
#     for i in range(len(seq1)-1, -1, -1):
#         num1 = seq1[i]
#         num2 = seq2[i]
        
#         soma = num1 + num2 + carry
        
#         carry = soma // 10
#         resultado.append(soma % 10)
    
#     if carry:
#         resultado.append(carry)
    
#     resultado.reverse()
    
#     return resultado

# sequencia1 = [1, 8, 2, 4, 3, 4, 2, 5, 1]
# sequencia2 = [3, 3, 7, 5, 2, 3, 3, 7]

# maxlen = max(len(sequencia1), len(sequencia2))
# sequencia1 = [0] * (maxlen - len(sequencia1)) + sequencia1
# sequencia2 = [0] * (maxlen - len(sequencia2)) + sequencia2

# resultado = somar_sequencias(sequencia1, sequencia2)

# print("Resultado da soma:")
# print(resultado)




# Matrizes



# EXERCICIO 1

# matriz = []

# for i in range(2):
#     linha = []
#     print(f"Digite os 4 números inteiros para a linha {i+1}:")
#     for j in range(4):
#         numero = int(input(f"Elemento ({i+1}, {j+1}): "))
#         linha.append(numero)
#     matriz.append(linha)

# print("Matriz 2x4:")
# for linha in matriz:
#     print(linha)




# EXERCICIO 2

# matriz = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]

# somaColuna1 = matriz[0][0] + matriz[1][0] + matriz[2][0] + matriz[3][0]

# produtoLinha1 = matriz[0][0] * matriz[0][1] * matriz[0][2] * matriz[0][3]

# total = 0
# for linha in matriz:
#     total += sum(linha)

# diagonal= matriz[0][0] * matriz[1][1] * matriz[2][2] * matriz[3][3]

# # Exibindo os resultados
# print(f"Soma dos elementos da primeira coluna: {somaColuna1}")
# print(f"Produto dos elementos da primeira linha: {produtoLinha1}")
# print(f"Soma de todos os elementos: {total}")
# print(f"Produto da diagonal principal: {diagonal}")




# EXERCICIO 3

# A = [
#     [-10, 1, 4, 6],
#     [2, 3, 2, 8]
# ]

# B = [
#     [1, 8, 4, -1],
#     [0, 6, 3, -3]
# ]

# C = []

# for i in range(len(A)):
#     linha = []
#     for j in range(len(A[i])):
#         linha.append(A[i][j] + B[i][j])
#     C.append(linha)

# print("Resultado da soma A + B:")
# for linha in C:
#     print(linha)




# EXERCICIO 4

# A = [
#     [2, -3],
#     [-1, 4]
# ]

# oposta = []

# for i in range(len(A)):
#     linha = []
#     for j in range(len(A[i])):
#         linha.append(-A[i][j])
#     oposta.append(linha)


# print("Matriz A:")
# for linha in A:
#     print(linha)

# print("Matriz oposta -A:")
# for linha in oposta:
#     print(linha)




# EXERCICIO 5

# A = [
#     [-7, 8],
#     [4, 9],
#     [2, 1]
# ]

# At = []


# for j in range(len(A[0])):
#     linha = []
#     for i in range(len(A)):
#         linha.append(A[i][j])
#     At.append(linha)


# print("Matriz A:")
# for linha in A:
#     print(linha)

# print("Matriz transposta At:")
# for linha in At:
#     print(linha)




# EXERCICIO 6

# A = [
#     [2, 3, 1],
#     [-1, 0, 2]
# ]

# B = [
#     [1, -2],
#     [0, 5],
#     [4, 1]
# ]

# C = []

# for i in range(len(A)):
#     linha = []
#     for j in range(len(B[0])):
#         soma = 0
#         for k in range(len(A[0])):
#             soma += A[i][k] * B[k][j]
#         linha.append(soma)
#     C.append(linha)

# print("Resultado da multiplicação A x B:")
# for linha in C:
#     print(linha)




# EXERCICIO 7

# N = int(input("Informe o tamanho da matriz identidade (ordem N): "))

# identidade = []

# for i in range(N):
#     linha = []
#     for j in range(N):
#         if i == j:
#             linha.append(1)  
#         else:
#             linha.append(0)
#     identidade.append(linha)

# print("Matriz Identidade de ordem", N, ":")
# for linha in identidade:
#     print(linha)



# EXERCICIO 8

# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# def rotacionar90(matriz):
#     N = len(matriz)
#     novaMatriz = [[0] * N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             novaMatriz[j][N-1-i] = matriz[i][j]
#     return novaMatriz

# def rotacionar180(matriz):

#     matriz90 = rotacionar90(matriz)
#     return rotacionar90(matriz90)

# def rotacionar270(matriz):
#     matriz90 = rotacionar90(matriz)
#     matriz180 = rotacionar90(matriz90)
#     return matriz180

# def exibirMatriz(matriz):
#     for linha in matriz:
#         print(linha)


# print("Matriz original:")
# exibirMatriz(matriz)

# print("Matriz rotacionada em 90°:")
# matriz90 = rotacionar90(matriz)
# exibirMatriz(matriz90)

# print("Matriz rotacionada em 180°:")
# matriz180 = rotacionar180(matriz)
# exibirMatriz(matriz180)

# print("Matriz rotacionada em 270°:")
# matriz270 = rotacionar270(matriz)
# exibirMatriz(matriz270)




# EXERCICIO 9

# tempo = [
#     [0, 2, 11, 6, 15, 11, 1],  
#     [2, 0, 7, 12, 4, 2, 15],   
#     [11, 7, 0, 11, 8, 3, 13],  
#     [6, 12, 11, 0, 10, 2, 1],  
#     [15, 4, 8, 10, 0, 5, 13],  
#     [11, 2, 3, 2, 5, 0, 14],  
#     [1, 15, 13, 1, 13, 14, 0]   
# ]

# def consultarTempo(cidade1, cidade2):
#     return tempo[cidade1 - 1][cidade2 - 1]

# def tempoTotal(rota):
#     tempo_total = 0
#     for i in range(len(rota) - 1):
#         tempo_total += consultarTempo(rota[i], rota[i + 1])
#     return tempo_total

# print("Consulta de tempo entre duas cidades:")
# cidade1 = int(input("Digite a cidade de partida (1 a 7): "))
# cidade2 = int(input("Digite a cidade de destino (1 a 7): "))
# tempoViagem = consultarTempo(cidade1, cidade2)
# print(f"O tempo necessário para percorrer da cidade {cidade1} à cidade {cidade2} é: {tempoViagem} unidades de tempo.")

# print("Consulta de tempo total para um percurso entre várias cidades:")
# rota = []
# while True:
#     cidade = int(input("Digite o número da cidade (1 a 7), ou 0 para encerrar: "))
#     if cidade == 0:
#         break
#     if 1 <= cidade <= 7:
#         rota.append(cidade)
#     else:
#         print("Cidade inválida, digite uma cidade entre 1 e 7.")


# if len(rota) > 1:
#     tempoTotal = tempoTotal(rota)
#     print(f"O tempo total para cumprir o trajeto pelas cidades {rota} é: {tempoTotal} unidades de tempo.")
# else:
#     print("Não foi possível calcular o tempo total, pois a rota precisa de pelo menos 2 cidades.")




# EXERCICIO 10

# def gerarPascal(n):
#     pascal = [[0] * n for _ in range(n)]
    
#     for i in range(n):
#         pascal[i][0] = 1  
#         pascal[i][i] = 1  
    
#     for i in range(2, n):  
#         for j in range(1, i):
#             pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    
#     for i in range(n):
#         for j in range(i + 1): 
#             print(pascal[i][j], end="\t")
#         print() 

# n = int(input("Informe a ordem do Triângulo de Pascal: "))

# gerarPascal(n)
