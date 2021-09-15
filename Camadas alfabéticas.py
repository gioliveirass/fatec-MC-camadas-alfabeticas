# Importando bibliotecas
import string

# Criando lista com o alfabeto
alfabetoMinusculo = list(string.ascii_lowercase)
alfabetoMaiusculo = list(string.ascii_uppercase)
alfabetoTotal = alfabetoMaiusculo + alfabetoMinusculo

# ===================
# Funções
# ===================

# =========================================================================================================================================

# Verifica se N está entre 1 e 52
def verifica_N(n):
    while n<=0 or n>52:
        n = int(input('O valor de N precisa estar entre 1 e 52. Por favor, insira novamente: '))
    return n

# =========================================================================================================================================

# Inicializa a matriz das camadas alfabéticas
def inicializa_matrizDasCamadas(n):
    dimencaoMatriz = n*2+1 # Exemplo: n = 2 -> matriz = [5, 5] ou seja [n*2+1, n*2+1]
    matrizDasCamadas_inicializada = []
    
    for linhaQueAMatrizDeveiraTer in range(0, dimencaoMatriz): # Exemplo: vai de 0 a 4, ou seja 5 linhas
        linhaNova = [] # Cria linha nova (para cada linha que a matriz deveria ter, cria-se uma linha nova)

        # Cria as colunas com A dentro da linha
        for colunaDaMatriz in range(0, dimencaoMatriz):
            linhaNova.append(alfabetoTotal[0]) # Adiciona uma coluna com a letra "A" na linha criada
            
        matrizDasCamadas_inicializada.append(linhaNova) # Adiciona na matriz a linha com a coluna criada
    
    return matrizDasCamadas_inicializada

# =========================================================================================================================================

# Constrói as camadas alfabéticas na matriz
def constroi_matrizDasCamadas(n, matriz_inicializada):
    letraAtual = 1 # O A (0) já foi preenchido
    dimencaoMatriz = n*2+1 # Exemplo: n = 2 -> matriz = [5, 5] ou seja [n*2+1, n*2+1]

    for quantidadeCamadasPreenchidas in range(1, n): # Começa no 1 porque a camada 0 já foi preenchida
        for linha in range(quantidadeCamadasPreenchidas, dimencaoMatriz - quantidadeCamadasPreenchidas): # Excluí as camadas que já foram preenchidas
            for coluna in range(quantidadeCamadasPreenchidas, dimencaoMatriz - quantidadeCamadasPreenchidas):
                matriz_inicializada[linha][coluna] = alfabetoTotal[letraAtual]
        letraAtual = letraAtual + 1

    # Coloca o * na metade intera da dimenção da matriz, ou seja em n
    matriz_inicializada[n][n] = "*"

    return matriz_inicializada
    
# =========================================================================================================================================

# Imprime as camadas alfabéticas
def imprime_matrizDasCamadas(n, matriz):
    dimencaoMatriz = n*2+1 # Exemplo: n = 2 -> matriz = [5, 5] ou seja [n*2+1, n*2+1]
    
    for linhaDaMatriz in range(0, dimencaoMatriz):
        print(*matriz[linhaDaMatriz], sep=' ') # Impime as linhas da matriz separadas por espaço

# =========================================================================================================================================

# ===================
# Programa principal
# ===================

N_digitado = int(input('Insira um valor N entre 1 e 52: '))
n = verifica_N(N_digitado)
matrizDasCamadas_inicializada = inicializa_matrizDasCamadas(n)
matrizDasCamadas = constroi_matrizDasCamadas(n, matrizDasCamadas_inicializada)
imprime_matrizDasCamadas(n, matrizDasCamadas)



