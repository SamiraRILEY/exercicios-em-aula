#pedir um numero inteiro
#verificar  se é par e armazenarem um boolean
#mostrar pro usuário o numero e o boolean

numero = int(input("digite um numero inteiro:"))
e_par = True if numero%2==0 else False

print(f"o numero é {numero} e o boolean é {e_par}")