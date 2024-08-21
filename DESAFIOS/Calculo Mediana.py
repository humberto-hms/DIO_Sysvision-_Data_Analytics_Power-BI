# Solicita ao usuário uma lista de números separados por vírgula e os converte para ponto flutuante
numeros = list(map(float, input().split(',')))

# Define a função para calcular a mediana de uma lista de números
def calcular_mediana(numeros):
    # Ordena a lista de números em ordem crescente
    numeros_ordenados = sorted(numeros)
    # Obtém o comprimento da lista ordenada
    n = len(numeros_ordenados)
    # Calcula o ponto médio da lista
    ponto_medio = n // 2

    # Verifica se a quantidade de números é ímpar
    if n % 2 == 1:
        # Se for ímpar, retorna o valor no meio da lista
        return numeros_ordenados[ponto_medio]
    else:
        # Se for par, retorna a média dos dois valores do meio da lista
        return (numeros_ordenados[ponto_medio - 1] + numeros_ordenados[ponto_medio]) / 2

# Chama a função calcular_mediana com a lista de números como argumento e imprime o resultado
print(calcular_mediana(numeros))
