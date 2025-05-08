# Pedir pro usuário inserir um código de produto
# Usar match case pra encontrar o produto pelo código
# 1 = Eletrônicos, 2 = Roupas, 3 = Alimentos, 4 = Livros, 5 = Brinquedos, outros = Código inválido

cod_produto = int(input("Digite o código do produto: "))

match cod_produto:
    case 1:
        print("Eletrônicos")
    case 2:
        print("Roupas")
    case 3:
        print("Alimentos")
    case 4:
        print("Livros")
    case 5:
        print("Brinquedos")
    case _:
        print("Código inválido")