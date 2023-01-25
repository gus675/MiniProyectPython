from funcionesCATEGORIA import*

DEMO()
Zero()
listaDeCat = []

print("\nBIENVENIDO A TU BASE DE CARGA DE CATEGORIAS!!")
print("Comenzaremos la carga...")

while(True):

    MENU()
    opc = int(input(""))
    if(opc== 4):
        print("Gracias por utilizar 'TU BASE DE CARGA DE CATEGORIAS'!! Hasta pronto...")
        exit()

    elif(opc==1):
        print('Esta es TU BASE DE CARGA DE CATEGORIAS')
        with open('cat10bis.json', 'r') as archivo:
            datosCat = archivo.read()
        objLista = (json.loads(datosCat))
        print(json.dumps(objLista,indent=2))
    
    elif(opc == 2):
        opc = int(input("Indica cuantas CATEGORIAS deseas CARGAR >>> "))
        listaDeCat.clear()
        for i in range(opc):
            crear_nuevaCat()
            persistir()
        print(">>>>> HAS REALIZADO LA CARGA EXITOSAMENTE. FELICITACIONES!! <<<<<")

    elif(opc == 3):
        print("\n")
        print("<<< Este es el EDITOR DE DATOS de TU BASE DE CATEGORIAS >>>\n")
        print("para MODIFICAR registros < 1 >\npara ELIMINAR CATEGORIAS < 2 >\n")
        opcEdit = int(input("Ingrese la opcion deseada >>> \n"))

        if(opcEdit == 1):
            editarCat()
        elif(opcEdit==2):
            eliminar()
        else:
            print("\nNO SE ELIMINO NINGUN REGISTRO")
            exit()
    else:
        print("\n OPCION INVALIDA")
        input('Presiona ENTER para VOLVER AL MENU')
        exit()

