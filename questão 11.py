# Pedir 3 números para o usuário
# Inserir numa lista
# Ordenar a lista
# Mostrar pro usuário

numeros = []

for i in range(3):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

numeros.sort()

print(numeros)