from funcionesAUTOR import *

DEMO()
Zero()

print("\n>>>>> BIENVENIDO A TU BASE DE CARGA DE ESCRITORES!! <<<<<")
print("Comenzaremos la carga...")
listaDeEscritores = []
while(True):

    MENU()
    opc = int(input(""))
    if(opc== 4):
        print("Gracias por utilizar 'TU BASE DE CARGA DE ESCRITORES'!! Hasta pronto...")
        exit()

    elif(opc==1):
        os.system('cls')
        print("\n>>>>> TU BASE DE ESCRITORES <<<<<")
        with open('Aut10bis.json', 'r') as archivo:
            baseAut = archivo.read()
        objLista = (json.loads(baseAut))
        print(json.dumps(objLista,indent=2))

    elif(opc == 2):
        opc = int(input("Indica cuantos AUTORES deseas CARGAR >>> "))
        for i in range(opc):
            crearNuevoAut()
            persistir()
        print(">>>>> HAS REALIZADO LA CARGA EXITOSAMENTE. FELICITACIONES!! <<<<<")
        input('Presiona ENTER para VOLVER AL MENU')

    elif(opc == 3):
        os.system('cls')
        print("\n<<< Este es el EDITOR DE DATOS de TU BASE DE ESCRITORES >>>\n")
        print("para MODIFICAR registros < 1 >\npara ELIMINAR AUTORES < 2 >\n")
        opcEdit = int(input("Ingrese la opcion deseada >>> \n"))
        if(opcEdit == 1):
            editorAutor()
        
        elif(opcEdit==2):
            eliminarAut()
        else:
            print("\n OPCION INVALIDA")
            exit
    else:
        print("Opcion invalida. Intentelo nuevamente.")
        exit 