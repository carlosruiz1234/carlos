import random


victorias = 0 
derrotas = 0
juegos = 0 
print("bienvenido al juego contra la banca")
print("""reglas:....
Reglas: Si tu carta es mayor que la de la banca, ganas la ronda.
El juego termina si ganas 5 veces, pierdes 3 veces o decides retirarte.""")

while True:
    print(f"\n victorias: {victorias} y Derrotas: {derrotas}")
    decision = input("quieres jugar esta ronda? (si/no): ").lower()

    if decision  == 'no':
        print("te has retirado del juego.")
        break

    cartaJugador = random.randint(1,13)
    cartaBanca = random.randint(1,13)

    print(f"tu carta: {cartaJugador}")
    print(f"carta de la banca; {cartaBanca}")

    if cartaJugador > cartaBanca:
        victorias += 1
        print("ganaste esta ronda")
    elif cartaJugador < cartaBanca:
        derrotas += 1
        print("has perdido esta ronda")
    else:
        print("empate.no suma ni resta puntos") 

    if victorias == 5:
        print ("\n FELICIDADES!!! has ganado")
        break
    if derrotas == 3:
        print("\n Has perdido tres veces la banca gana")
        break
print("resultado final", victorias,"victorias")
print(derrotas,"derrotas")