HorasNormales = int(input('ingrese el numero de horas trabajadas: '))

HoraNormal = 6200
hora1 = 12400
hora2 = 18600
base = 40*6200

resta = (HorasNormales-40)
resta1 = (HorasNormales-48)

totales = (HorasNormales*HoraNormal)
prim8 = (resta*hora1)
segunda8 = (resta1*hora2)
num8 = 99200



if HorasNormales < 40:
    print(totales)
elif HorasNormales <=48:
    print("horas extrasx2 ",resta*hora1)
else:
    segunda8 > 48
    print("horas extra x2: ",(base))
    print(("horas extra x3: "),(num8+segunda8))
    var1 = num8+segunda8
    print (base +var1 )

    
    