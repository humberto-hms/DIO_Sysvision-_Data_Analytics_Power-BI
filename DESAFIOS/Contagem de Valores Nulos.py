# Receber a lista do usuário
entrada = input()

# Converter a string de entrada em uma lista de valores
lista = [int(x.strip()) if x.strip().isdigit() else None for x in entrada.split(',')]

# TODO: Conte quantos elementos são None usando a função count:
contador_nulos = lista.count(None)

# Exibir o resultado
print(contador_nulos)