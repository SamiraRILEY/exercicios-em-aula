#pedir um texto pro usuário
#verificar se esse texto tem mais de 5 letras e armazenar o boolean
#mostrar pro usuario o texto e o boolean

texto = input("digite um texto: ")
tamanho_texto = len(texto)
mais_de_cinco = None

if tamanho_texto > 5:
    mais_de_cinco = True
else:
    mais_de_cinco = False

print("o texto é", texto, " o boolean é", mais_de_cinco)
