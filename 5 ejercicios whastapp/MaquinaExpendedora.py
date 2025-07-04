import time 
Total = 0

print("BIenvenido a la maquina expendedroa")
print("estas son las siguientes opciones: ")
print("1.cafe (3.000) ")
print("2.te (2.500) ")
print("3.jugo (3.500) ")
print("finalizar compra")
while True:
    opcion = int(input("seleccione una opcion del 1 al 3 o 0 para terminar: "))

    match opcion:
        case 1:
            print("has seleccionado cafe  3000")
            Total += 3000
        case 2:
            print("has seleccionado te  2500")
            Total += 2500
        case 3:
            print("has seleccionado jugo  3500")
            Total += 3500
        case 0:
            print("finalizando compra...")
            break
        case _:
            print("opcion no valida.Intenta de nuevo ")
time.sleep(2)
print(f"\n total a pagar : ${Total}")
        