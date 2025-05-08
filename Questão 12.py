# Pedir a idade da pessoa e o preço do ingresso
# Aplicar desconto de 50% para menores de 12 anos,
# 30% para maiores de 60 anos e 10% para estudantes

idade = int(input("Qual sua idade? "))
e_estudante = input("Você é estudante? (S para Sim, N para Não)")

preco_inteiro = 100
preco_desconto = None

if idade < 12:
    preco_desconto = preco_inteiro * 0.5
elif idade > 60:
    preco_desconto = preco_inteiro * 0.7
elif e_estudante == "S":
    preco_desconto = preco_inteiro * 0.9

print(f"O valor do ingresso é", preco_desconto or preco_inteiro)