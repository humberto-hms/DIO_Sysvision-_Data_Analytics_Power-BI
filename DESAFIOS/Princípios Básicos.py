# Recebe a lista do usuário
entrada = input()
# Converte a string de entrada em uma lista de números
lista = [int(x.strip()) for x in entrada.split(',')]

# TODO: Remova as duplicatas:
lista_unica = list (set(lista))


# É Exibido a nova lista sem valores duplicados
print(lista_unica)