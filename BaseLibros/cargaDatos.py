
class CargadorDeDatos:
    def __init__(self):
        pass

    def cargarLibro(self):
        with open('contadorLibros.txt', 'r') as archivo:
            UltimoNid = int(archivo.read())
        id = UltimoNid +1
        with open('contadorLibros.txt', 'w') as archivo:
            archivo.write(str(id))
        titulo = input("Titulo: ")
        autor = input("Autor: " )    
        print("\n>>>>> Estas son las CATEGORIAS LITERARIAS:\nPOESIA (1)\nTEATRO (2)\nNARRATIVA (3)\nENSAYO (4)\nARTICULO (5)\n")
        indice = int(input("Ingrese el numero de categoria elegida >> "))
        listaCatLit = ["POESIA","TEATRO","NARRATIVA","ENSAYO", "ARTICULO"]
        indice -= 1
        categoria = (listaCatLit[indice])

        return (id,titulo,autor,categoria)