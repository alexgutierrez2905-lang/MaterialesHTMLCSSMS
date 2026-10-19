empleados = {
    "nombre": ["Andrea", "Pedro"],
    "cargo": ["Gerente", "Contador"],
    "id": [789, 123]
}

ubicacion = {
    "empleado": [789],
    "piso": [5],
    "oficina": [1]
}


def registrar_empleado():

    nombre = input("Digite su nombre: ")
    cargo = input("Digite su cargo: ")
    id = int(input("Digite su ID: "))

    if id not in empleados["id"]:

        empleados["nombre"].append(nombre)
        empleados["cargo"].append(cargo)
        empleados["id"].append(id)

        print("Empleado registrado")

    else:
        print("ID repetido")


def mover_empleado():

    id = int(input("Digite el ID: "))
    piso = int(input("Digite el piso: "))
    oficina = int(input("Digite la oficina: "))

    if id in empleados["id"]:

        ubicacion["empleado"].append(id)
        ubicacion["piso"].append(piso)
        ubicacion["oficina"].append(oficina)

        print("Movimiento registrado")

    else:
        print("Empleado no existe")


def ultimo_movimiento():

    id = int(input("Digite el ID: "))

    posicion = -1

    for i in range(len(ubicacion["empleado"])):

        if ubicacion["empleado"][i] == id:

            posicion = i

    if posicion != -1:

        print("Piso:", ubicacion["piso"][posicion])
        print("Oficina:", ubicacion["oficina"][posicion])

    else:
        print("El empleado no tiene movimientos")


while True:

    print("\nMENU")
    print("1. Registrar empleado")
    print("2. Mover empleado")
    print("3. Ver último movimiento")
    print("4. Salir")

    opcion = input("Digite una opción: ")

    if opcion == "1":
        registrar_empleado()

    elif opcion == "2":
        mover_empleado()

    elif opcion == "3":
        ultimo_movimiento()

    elif opcion == "4":
        break

    else:
        print("Opción incorrecta")
