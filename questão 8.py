#adicionar uma nova fruta
#remover uma fruta
#mostrar pro usuário a lista final

frutas = ["banana", "abacaxi", "marajujá"]
fruta = input(f"qual fruta voce quer adiconar na lista? {frutas}")
frutas.append(fruta)         #adiciona
frutas.pop(1)
print("a lista de frutas é",frutas)