from funcionesLIBRO import *

DEMO()
Zero()

os.system("cls")
print("\nBIENVENIDO A TU BASE DE CARGA DE LIBROS!!")
print("Comenzaremos la carga...")
listaDelibros = []
while(True):

    MENU()
    opc = int(input(""))

    if(opc== 4):
        print("Gracias por utilizar 'TU BASE DE CARGA DE LIBROS'!! Hasta pronto...")
        exit()

    elif(opc==1):
        print("\n>>>>> TU BASE DE CARGA DE LIBROS <<<<<")
        with open('datos10bis.json', 'r') as archivo:
            datosLibros = archivo.read()
        objLista = (json.loads(datosLibros))
        for dic in objLista:
            print(dic)
            

    elif(opc == 2):
        opc = int(input("Indica cuantos LIBROS deseas CARGAR >>> "))
        listaDelibros.clear()
        for i in range(opc):
            crear_nuevoLibro()
            persisitirDatos()
        print(">>>>> HAS REALIZADO LA CARGA EXITOSAMENTE. FELICITACIONES!! <<<<<")
        input('Presiona ENTER para VOLVER AL MENU')
     
    elif(opc == 3):
        os.system('cls')
        print("<<< Este es el EDITOR DE DATOS de TU BASE DE LIBROS >>>\n")
        print("para MODIFICAR registros < 1 >\npara ELIMINAR libros < 2 >\n")
        opcEdit = int(input("Ingrese la opcion deseada >>> \n"))
        if(opcEdit == 1):
            editorLibro()
           
        elif(opcEdit==2):
            eliminarLibro()
        else:
            print("\nNO SE EDITO / ELIMINO NINGUN REGISTRO")
            exit
    else:

        print("\n OPCION INVALIDA")
        exit