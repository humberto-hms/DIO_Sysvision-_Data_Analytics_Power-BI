# Receber a lista do usuário
entrada = input()
# Convertee a string de entrada em uma lista de números
lista = [float(x.strip()) for x in entrada.split(',')]

# Calcula a soma dos números na lista
soma = sum(lista)
# Calcula a quantidade de elementos na lista
quantidade = len(lista)
# TODO: Calcule a média aritmética:
media = soma / quantidade

# Exibir a média com duas casas decimais
print(f'{media:.1f}')
