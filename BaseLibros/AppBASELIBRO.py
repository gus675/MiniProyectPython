import os
from baseLibro import BaseLibro
from cargaDatos import CargadorDeDatos

os.system("cls")

import os, json
clear = lambda : os.system("cls")
clear()

print("\nBIENVENIDO A TU BASE DE CARGA DE LIBROS!!")
print("Comenzaremos la carga...")

with open ("datos10bis.json", "w") as archivo:
    pass

LibroDEMO = {
    'id': 0,
    'titulo': 'El Tunel',
    'autor': 'Ernesto Sabato',
    'categoria': 'Narrativa'
}

listaDelibros = []

vacio = os.stat("datos10bis.json").st_size == 0
True
if vacio == True:
    listaDelibros.append(LibroDEMO)
    with open ("datos10bis.json", "w") as archivo:
        json.dump(listaDelibros, archivo, indent= 2)
    listaDelibros =[]

with open ("contadorLibros.txt", "w") as archivo:
    pass

Zero = 0
vacio2 = os.stat("contadorLibros.txt").st_size == 0
True
if vacio2 == True:
    with open ("contadorLibros.txt", "w") as archivo:
        json.dump(Zero, archivo, indent= 2)
else:
    with open('datos10bis.json', 'r') as archivo:
        datosLibros = archivo.read()
    objLista = (json.loads(datosLibros))
    
    ultimoReg = objLista[-1]
    
    with open('contadorLibros.txt', 'w') as archivo:
        archivo.write(str(ultimoReg['id']))

while(True):
    
    print("\nConsultar TU BASE DE CARGA DE LIBROS >>> 1")
    print("Cargar LIBRO >>> 2")
    print("Editar datos de TU BASE DE LIBROS >>> 3")
    print("SALIR >>> 4")
    opc = int(input(""))
    if(opc== 4):
        print("Gracias por utilizar 'TU BASE DE CARGA DE LIBROS'!! Hasta pronto...")
        exit()
    elif(opc == 1):

        with open('datos10bis.json', 'r') as archivo:
            baseLibros = archivo.read()
        objLista = (json.loads(baseLibros))
        for dic in objLista:
            print(dic)

    elif(opc == 2):
        opc = int(input("Indica cuantos LIBROS deseas CARGAR >>> "))
        for i in range(opc):

            nuevoCargador = CargadorDeDatos()
            id,titulo,autor,categoria = nuevoCargador.cargarLibro()
            nuevoLibro = BaseLibro(id,titulo,autor,categoria)

            nuevoLibro.crear_nuevoLibro()
            nuevoLibro.persistirDatos()
                
            print(">>>>> HAS REALIZADO LA CARGA EXITOSAMENTE. FELICITACIONES!! <<<<<")

        else:
            exit
        input('Presiona ENTER para VOLVER AL MENU')
     
    elif(opc == 3):
        print("\n")
        print("<<< Este es el EDITOR DE DATOS de TU BASE DE LIBROS >>>\n")
        print("para MODIFICAR registros < 1 >\npara ELIMINAR libros < 2 >\n")
        opcEdit = int(input("Ingrese la opcion deseada >>> \n"))

        if(opcEdit == 1):
            nuevoLibro.editorLibro()

        elif(opcEdit==2):
            nuevoLibro.eliminarLibro()
        else:
            print("\n OPCION INVALIDA")
            exit
            
    else:
        print("Opcion invalida. Intentelo nuevamente.")
        exit()