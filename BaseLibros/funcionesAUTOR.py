import os, json
clear = lambda : os.system("cls")
clear()

def DEMO():
    EscritorDEMO =  {
        "id": 0,
        "nombre completo": "Jules Gabriel Verne",
        "natalicio": "8 de febrero de 1828",
        "nacionalidad": "Francia",
        "obras": [
          "La vuelta al mundo en ochenta dias",
          "Viaje al centro de la tierra",
          "Veintemil leguas de viaje submarino"
        ]
    }
    listaDeEscritores = []
    vacio = os.stat("Aut10bis.json").st_size == 0
    True
    if vacio == True:
        listaDeEscritores.append(EscritorDEMO)
        with open ("Aut10bis.json", "w") as archivo:
            json.dump(listaDeEscritores, archivo, indent= 2)
        listaDeEscritores =[]

def Zero():
    Zero = 0
    vacio2 = os.stat("idAut.txt").st_size == 0
    True
    if vacio2 == True:
        with open ("idAut.txt", "w") as archivo:
            json.dump(Zero, archivo, indent= 2)
    else:
        with open('Aut10bis.json', 'r') as archivo:
            datosAut = archivo.read()
        objLista = (json.loads(datosAut))
        ultimoReg = objLista[-1]
        with open('idAut.txt', 'w') as archivo:
            archivo.write(str(ultimoReg['id']))

class Autor:
    Ultimoid  = 0

    def __init__(self,id,nombreCompleto,Natalicio,nacionalidad,obras):
        self.id = id
        self.nombreCompleto = nombreCompleto
        self.Natalicio = Natalicio
        self.nacionalidad = nacionalidad
        self.obras = obras

def MENU():
    print("\nConsultar TU BASE DE ESCRITORES >>> 1")
    print("Cargar AUTOR >>> 2")
    print("Editar / Eliminar datos de TU BASE DE ESCRITORES >>> 3")
    print("SALIR >>> 4")

def crearAutor():
    with open('idAut.txt', 'r') as archivo:
        Ultimoid = int(archivo.read())
    id = Ultimoid +1
    with open('idAut.txt', 'w') as archivo:
        archivo.write(str(id))
    nombreCompleto = input("\nIngrese el NOMBRE (completo) de un ESCRITOR: ")
    Natalicio = input("Ingrese la fecha de nacimiento del mismo: ")
    nacionalidad = input("Pais donde nacio: ")
    print("Aqui puede cargar el TITULO de 3 de SUS OBRAS: ")
    obra1 = input("1) - ")
    obra2 = input("2) - ")
    obra3 = input("3) - ")
    obras = [obra1,obra2,obra3]
    return Autor(id,nombreCompleto,Natalicio,nacionalidad,obras)

def crearNuevoAut():
    nuevoAutor = crearAutor()
    nuevoAutor = {
            "id": nuevoAutor.id,
            "nombre completo": nuevoAutor.nombreCompleto,
            "natalicio": nuevoAutor.Natalicio, 
            "nacionalidad":nuevoAutor.nacionalidad,
            "obras":nuevoAutor.obras
            }
    listaDeEscritores = []
    listaDeEscritores.append(nuevoAutor)
    print(listaDeEscritores[-1])
    with open ("Aut10.json", "w") as archivo:
        json.dump(listaDeEscritores, archivo, indent=2)

def persistir():
    listaDeEscritores =[]      
    with open('Aut10bis.json', 'r') as archivo:
        datosAut = archivo.read()
    objLista = (json.loads(datosAut))
    with open('Aut10.json', 'r') as archivo:
        Autores = archivo.read()
    objListaAut = (json.loads(Autores))
    baseTotal = []
    for i in objLista:
        baseTotal.append(i)
    for i in objListaAut:
        baseTotal.append(i)
    with open ("Aut10bis.json", "w") as archivo:
        json.dump(baseTotal, archivo, indent=2)
    with open ("Aut10.json", "w") as archivo:
        pass
    listaDeEscritores.clear()
        
def editorAutor():
    print("Estos son los AUTORES cargados en TU BASE DE ESCRITORES:")
    with open('Aut10bis.json', 'r') as archivo:
        baseAut = archivo.read()
    objLista = (json.loads(baseAut))
    print(json.dumps(objLista,indent=2))
    opc = int(input("\nIngrese el NUMERO DE AUTOR q desea EDITAR >> "))
    editarReg = (objLista[opc])
    print(editarReg)
    print(f"El REGISTRO seleccionado para EDITAR es >>> {objLista[opc]}")
    print("MODIFICAR:\nID < 1 >\nNOMBRE < 2 >\nNATALICIO < 3 >\nNACIONALIDAD < 4 >\nOBRAS < 5\n >")
    opcItemModif = int(input(">>> "))
    if opcItemModif == 1:
        print('Id: ' , editarReg['id'])
        idNuevo = input("Escriba el nuevo ID que REEMPLAZARA al actual >> ")
        editarReg['id'] = idNuevo
    elif opcItemModif == 2:
        print('Nombre: ' + editarReg['nombre completo'])
        nombreNuevo = input("Escriba el nuevo NOMBRE que REEMPLAZARA al actual >> ")
        editarReg['nombre completo'] = nombreNuevo
    elif opcItemModif == 3:
        print('Natalicio: ' + editarReg['natalicio'])
        natalicioNuevo = input("Escriba el nuevo NATALICIO que REEMPLAZARA al actual >> ")
        editarReg['natalicio'] = natalicioNuevo
    elif opcItemModif == 4:
        print('Nacionalidad: '+ editarReg['nacionalidad'])
        nacionalidadNueva = input("Escriba la nueva NACIONALIDAD que REEMPLAZARA a la actual >> ")
        editarReg["nacionalidad"] = nacionalidadNueva
    elif opcItemModif == 5:
        print('Obras: ' , editarReg['obras'])
        print("Escriba la/las que OBRA/S que REEMPLAZARA/N al registro actual  >> ")
        obra1 = input("1) - ")
        obra2 = input("2) - ")
        obra3 = input("3) - ")
        obrasModif = [obra1,obra2,obra3]
        editarReg["obras"] = obrasModif
    else:
        print("\nOPCION INVALIDA")
        exit    
    print(editarReg)
    with open ("Aut10bis.json", "w") as archivo:
        json.dump(objLista, archivo, indent= 2)

def eliminarAut():
    print("Estos son los AUTORES cargados en TU BASE DE ESCRITORES:")
    with open('Aut10bis.json', 'r') as archivo:
        baseAut = archivo.read()
    objLista = (json.loads(baseAut))
    print(json.dumps(objLista,indent=2))
    ELIMINAR = int(input("\nIngrese el NUMERO de AUTOR que desea ELIMINAR >>> "))
    numeroReg = (objLista[ELIMINAR])
    print(f"El REGISTRO seleccionado para ELIMIMAR es >>> {numeroReg}")
    confirmar = input("ELIMINARA un AUTOR de la base // CONFIRMA? S / N  ")
    if confirmar.upper() == "S":
        print(f"\nEl ESCRITOR numero [{ELIMINAR}] fue ELIMINADO\n")
        #### del objLista[ELIMINAR-1] NOTA: Si se ELIMINA PIERDE CORRELACION DE NUMERO ID
        ELIMINADO = (f"Reg. {ELIMINAR} ELIMINADO")
        objLista[ELIMINAR] = (ELIMINADO)
        with open ("Aut10bis.json", "w") as archivo:
            json.dump(objLista, archivo, indent= 2)
        with open('Aut10bis.json', 'r') as archivo:
            baseAut = archivo.read()
        objLista = (json.loads(baseAut))
        print(json.dumps(objLista,indent=2,))
    else:
        print("\nNO SE ELIMINO NINGUN REGISTRO")
        exit
    