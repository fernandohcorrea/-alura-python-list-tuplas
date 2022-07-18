idades = []

idades.append(8)
idades.append(12)
idades.append(24)
idades.append(28)
idades.append(7)
idades.append(15)


print(15 in idades)
print(33 in idades)

if 33 in idades:
    idades.remove(33)


idades_mais_um = [(idade+1) for idade in idades if idade > 23]
print(idades)
print(idades_mais_um)



def processaLista (list = None):
    if list == None:
        lista = []
    lista.append(6)
    print(len(lista))

processaLista()
processaLista()
processaLista()

