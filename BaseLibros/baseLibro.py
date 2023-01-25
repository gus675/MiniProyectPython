import json
from libro import Libro

class BaseLibro(Libro):

    def crear_nuevoLibro(self):
        nuevoLibro = {
                'id': self.id,
                'titulo': self.titulo,
                'autor': self.autor,
                'categoria': self.categoria
                }
        listaDelibros = []
        listaDelibros.append(nuevoLibro)
        print(listaDelibros)
        with open ("datos10.json", "w") as archivo:
            json.dump(listaDelibros, archivo, indent=2)

    def persistirDatos(self):
        listaDelibros = []
        with open('datos10bis.json', 'r') as archivo:
            datosLibros = archivo.read()
        objLista = (json.loads(datosLibros))
        with open('datos10.json', 'r') as archivo:
            libros = archivo.read()
        objListalibros = (json.loads(libros))
        baseTotal = []
        for i in objLista:
            baseTotal.append(i)
        for i in objListalibros:
            baseTotal.append(i)
        with open ("datos10bis.json", "w") as archivo:
            json.dump(baseTotal, archivo, indent=2)
        with open ("datos10.json", "w") as archivo:
            pass
        listaDelibros.clear()

    def editorLibro(self):
        print("Estos son los LIBROS cargados en TU BASE DE CARGA DE LIBROS:\n")
        with open('datos10bis.json', 'r') as archivo:
            baseLibros = archivo.read()
        objLista = (json.loads(baseLibros))
        for dic in objLista:
            print(dic)
        opc = int(input("\nIngrese el NUMERO DE LIBRO q desea EDITAR >> "))
        numeroReg = (objLista[opc])
        print(numeroReg)
        print(f"El REGISTRO seleccionado para EDITAR es >>> {objLista[opc]}")
        print("\nMODIFICAR:\n ID < 1 >\nTITULO < 2 >\nAUTOR < 3 >\nCATEGORIA < 4 >")
        opcCambiarTitAutCat = int(input(">>> "))
        if opcCambiarTitAutCat == 1:
            print('Id: ' , numeroReg['id'])
            idNuevo = input("Escriba el nuevo ID que REEMPLAZARA al actual >> ")
            numeroReg['id'] = idNuevo
        elif opcCambiarTitAutCat == 2:
            print('Titulo: ' + numeroReg['titulo'])
            tituloNuevo = input("Escriba el nuevo TITULO que REEMPLAZARA al actual >> ")
            numeroReg['titulo'] = tituloNuevo
        elif opcCambiarTitAutCat == 3:
            print('Autor: '+ numeroReg['autor'])
            autorNuevo = input("Escriba el nuevo AUTOR que REEMPLAZARA al actual >> ")
            numeroReg["autor"] = autorNuevo
        elif opcCambiarTitAutCat == 4:
            print('Categoria: ' + numeroReg['categoria'])
            catNueva = input("Escriba la nueva CATEGORIA que REEMPLAZARA a la actual >> ")
            numeroReg["categoria"] = catNueva
        else:
            print("\nOPCION INVALIDA")
            exit
        print(numeroReg)
        with open ("datos10bis.json", "w") as archivo:
            json.dump(objLista, archivo, indent= 2)

    def eliminarLibro(self):
        print("Estos son los LIBROS cargados en TU BASE DE CARGA DE LIBROS:\n")
        with open('datos10bis.json', 'r') as archivo:
            baseLibros = archivo.read()
        objLista = (json.loads(baseLibros))
        for dic in objLista:
            print(dic)
        ELIMINAR = int(input("\nIngrese el NUMERO de LIBRO que desea ELIMINAR >>> "))
        #<< NOTA!!: Si ELIMINABA CON 'del objLista[ELIMINAR]' TODO EL REGISTRO PERDIA CORRELACION el NUMERO ID de LA LISTA DE DICCIONARIOS
        # POR ESO OPTE POR SOBREESCRIBIRLO >>
        numeroReg = (objLista[ELIMINAR])
        print(f"El REGISTRO seleccionado para ELIMIMAR es >>> {numeroReg}")
        confirmar = input("ELIMINARA un libro de la base // CONFIRMA? S / N  ")
        if confirmar.upper() == "S":
            print(f"\nLa CATEGORIA numero [{ELIMINAR}] fue ELIMINADA\n")
            ELIMINADO = (f"Reg. {ELIMINAR} ELIMINADO")
            objLista[ELIMINAR] = (ELIMINADO)
            with open ("datos10bis.json", "w") as archivo:
                json.dump(objLista, archivo, indent= 2)
            with open('datos10bis.json', 'r') as archivo:
                baseLibros = archivo.read()
            objLista = (json.loads(baseLibros))
        else:
            print("\nNO SE ELIMINO NINGUN REGISTRO")
            input('Presiona ENTER para VOLVER AL MENU')