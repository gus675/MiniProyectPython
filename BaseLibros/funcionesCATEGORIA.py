import os, json
clear = lambda : os.system("cls")
clear()

def DEMO():
    CategoriaDEMO = {
        "id": 0,
        "nombre": "POESIA",
        "descripcion": "Tiene ritmo y rima. Hace uso de elementos de valor simbolico. \nHace uso de las figuras literarias, entre las m\u00e1s empleadas esta la metafora. \nLa poesia moderna hace un extenso uso del verso libre y la rima asonante."
      }
    listaDeCat = []
    vacio = os.stat("cat10bis.json").st_size == 0
    True
    if vacio == True:
        listaDeCat.append(CategoriaDEMO)
        with open ("cat10bis.json", "w") as archivo:
            json.dump(listaDeCat, archivo, indent= 2)
        listaDeCat =[]

def Zero():
    Zero = 0
    vacio2 = os.stat("contadorCat.txt").st_size == 0
    True
    if vacio2 == True:
        with open ("contadorCat.txt", "w") as archivo:
            json.dump(Zero, archivo, indent= 2)
    else:
        with open('cat10bis.json', 'r') as archivo:
            datosCat = archivo.read()
        objLista = (json.loads(datosCat))
        ultimoReg = objLista[-1]
        with open('contadorCat.txt', 'w') as archivo:
            archivo.write(str(ultimoReg['id']))

class Categoria:
    UltimoId = 0
    
    def __init__(self,id,nombre,descripcion):
        self.id = id 
        self.nombre = nombre
        self.descripcion = descripcion

def MENU():
    print("\nConsultar TU BASE DE CARGA DE CATEGORIAS >>> 1")
    print("Cargar CATEGORIA >>> 2")
    print("Editar / Eliminar datos de TU BASE DE CARGA DE CATEGORIAS >>> 3")
    print("SALIR >>> 4")

def crearCat():
    with open('contadorCat.txt', 'r') as archivo:
        UltimoNid = int(archivo.read())
    id = UltimoNid +1
    with open('contadorCat.txt', 'w') as archivo:
        archivo.write(str(id))
    print("\n>>>>> Estas son las CATEGORIAS LITERARIAS:\nPOESIA (1)\nTEATRO (2)\nNARRATIVA (3)\nENSAYO (4)\nARTICULO (5)\n")
    indice = int(input("Ingrese el numero de categoria elegida >> "))
    listaCatLit = ["POESIA","TEATRO","NARRATIVA","ENSAYO", "ARTICULO"]
    indice -= 1
    nombre = (listaCatLit[indice])
    listaDefiniCat = ["Tiene ritmo y rima. Hace uso de elementos de valor simbolico. \nHace uso de las figuras literarias, entre las más empleadas esta la metafora. \nLa poesia moderna hace un extenso uso del verso libre y la rima asonante.",
    "El genero dramatico presenta un conflicto entre uno o varios personajes que se desarrolla mediante el dialogo.\nEl teatro se presenta: En un escenario, mediante una actuacion o puesta de escena de la obra.",
    "La narrativa tambien se conoce como género epico, el autor hace uso de la figura del narrador \npara contar los hechos protagonizados por unos personajes, presenta una realidad ficticia o \nrealidad representada como el mundo exterior u objetivo, ajeno al autor.",
    "Un ensayo es una obra literaria relativamente breve, de reflexion subjetiva pero bien informada,\nen la que el autor trata un tema por lo general humanistico de una manera personal y sin agotarlo,\ny donde muestra cierta voluntad de estilo, de forma mas o menos explicita, encaminada a \npersuadir al lector de su punto de vista sobre el asunto tratado.",
    "Es un estilo reciente de informacion, aparecido en el siglo XIX, en los medios modernos y la prensa escrita.\nAlgunos de los textos de opinion se pueden considerar periodismo literario, atendida su elaboracion formal \ny la presencia del punto de vista subjetivo del periodista. El genero periodistico se puede definir en \nfuncion del papel que juega el narrador o emisor del mensaje en relacion a la realidad observada."]
    descripcion = (listaDefiniCat[indice])
    return Categoria(id,nombre,descripcion)

def crear_nuevaCat():
    listaDeCat = []
    nuevaCat = crearCat()
    nuevaCat = {
        'id':nuevaCat.id,
        'nombre': nuevaCat.nombre,
        'descripcion':nuevaCat.descripcion
            }
    listaDeCat.append(nuevaCat)
    print(listaDeCat)
    with open ("cat10.json", "w") as archivo:
        json.dump(listaDeCat, archivo, indent=2)

def persistir():
    listaDeCat = []
    with open('cat10bis.json', 'r') as archivo:
        datosCat = archivo.read()
    objLista = (json.loads(datosCat))
    with open('cat10.json', 'r') as archivo:
        categorias = archivo.read()
    objListaCat = (json.loads(categorias))
    baseTotal = []
    for i in objLista:
        baseTotal.append(i)
    for i in objListaCat:
        baseTotal.append(i)
    with open ("cat10bis.json", "w") as archivo:
        json.dump(baseTotal, archivo, indent=2)
    with open ("cat10.json", "w") as archivo:
        pass
    listaDeCat.clear()

def editarCat():
    print("Estos son las CATEGORIAS cargadas en TU BASE DE CATEGORIAS:")
    with open('cat10bis.json', 'r') as archivo:
        baseCat = archivo.read()
    objLista = (json.loads(baseCat))
    print(json.dumps(objLista,indent=2))
    opc = int(input("\nIngrese el NUMERO DE CATEGORIA q desea EDITAR >> "))
    editarReg = (objLista[opc])
    print(f"El REGISTRO seleccionado para EDITAR es >>> {objLista[opc]}")
    print("\nMODIFICAR:\n ID < 1 >\nNOMBRE < 2 >\nDESCRIPCION < 3 >")
    opcCaT = int(input(">>> "))
    if opcCaT == 1:
        print('Id: ' , editarReg['id'])
        idNuevo = input("\nEscriba el nuevo ID que REEMPLAZARA al actual >> ")
        editarReg['id'] = idNuevo
    elif opcCaT == 2:
        print('Nombre: ' + editarReg['nombre'])
        nombreNuevo = input("\nEscriba el nuevo NOMBRE que REEMPLAZARA al actual >> ")
        editarReg['nombre'] = nombreNuevo
    elif opcCaT == 3:
        print('Descripcion: '+ editarReg['descripcion'])
        descripNuevo = input("\nEscriba DESCRIPCION que REEMPLAZARA a la actual >> ")
        editarReg["descripcion"] = descripNuevo
    else:
        print("\nOPCION INVALIDA")
        exit()
    print(editarReg)
    with open ("cat10bis.json", "w") as archivo:
        json.dump(objLista, archivo, indent= 2)

def eliminar():
    print("Estos son las CATEGORIAS cargadas en TU BASE DE CATEGORIAS:")
    with open('cat10bis.json', 'r') as archivo:
        baseCat = archivo.read()
    objLista = (json.loads(baseCat))
    print(json.dumps(objLista,indent=2))
    ELIMINAR = int(input("\nIngrese el NUMERO de CATEGORIA que desea ELIMINAR >>> "))
    numeroReg = (objLista[ELIMINAR])
    print(f"El REGISTRO seleccionado para ELIMIMAR es >>> {numeroReg}")
    confirmar = input("ELIMINARA una CATEGORIA de la base // CONFIRMA? S / N  ")
    if confirmar.upper() == "S":
        print(f"\nLa CATEGORIA numero [{ELIMINAR}] fue ELIMINADA\n")
        #### del objLista[ELIMINAR] NOTA: Si se ELIMINA PIERDE CORRELACION DE NUMERO ID
        ELIMINADO = (f"Reg. {ELIMINAR} ELIMINADO")
        objLista[ELIMINAR] = (ELIMINADO)
        with open ("cat10bis.json", "w") as archivo:
            json.dump(objLista, archivo, indent= 2)
        with open('cat10bis.json', 'r') as archivo:
            baseCat = archivo.read()
        objLista = (json.loads(baseCat))