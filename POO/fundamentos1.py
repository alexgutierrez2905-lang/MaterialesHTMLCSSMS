# SISTEMA DE RESERVAS DE HABITACIONES DE HOTEL

habitaciones = [
    {
        "id": 1,
        "numero": 101,
        "precio-noche": 150000,
        "capacidad": 2
    }
]

reservas = [
    {
        "id-habitacion": 1,
        "noches": 3,
        "total-pago": 450000
    }
]

# Como ya existe el ID 1, el siguiente será el 2
siguiente_id = 2


# REGISTRAR UNA HABITACIÓN
def registrar_habitacion(id_habitacion):

    numero = int(input("Digite el número de la habitación: "))
    precio_noche = float(input("Digite el precio por noche: "))
    capacidad = int(input("Digite la capacidad: "))

    numero_repetido = False

    for habitacion in habitaciones:
        if habitacion["numero"] == numero:
            numero_repetido = True

    if numero_repetido == False:

        nueva_habitacion = {
            "id": id_habitacion,
            "numero": numero,
            "precio-noche": precio_noche,
            "capacidad": capacidad
        }

        habitaciones.append(nueva_habitacion)

        print("Habitación registrada correctamente")
        print("ID asignado:", id_habitacion)

        id_habitacion = id_habitacion + 1

        return True, id_habitacion

    else:
        print("El número de habitación ya está registrado")

        return False, id_habitacion


# LISTAR TODAS LAS HABITACIONES
def listar_habitaciones():

    print("\n--- HABITACIONES REGISTRADAS ---")

    if len(habitaciones) == 0:
        print("No hay habitaciones registradas")

    else:
        for habitacion in habitaciones:
            print("ID:", habitacion["id"])
            print("Número:", habitacion["numero"])
            print("Precio por noche:", habitacion["precio-noche"])
            print("Capacidad:", habitacion["capacidad"])
            print("------------------------------")


# REALIZAR UNA RESERVA
def realizar_reserva():

    listar_habitaciones()

    id_habitacion = int(input("Digite el ID de la habitación a reservar: "))
    noches = int(input("Digite el número de noches: "))

    habitacion_encontrada = False

    for habitacion in habitaciones:

        if habitacion["id"] == id_habitacion:

            habitacion_encontrada = True

            total_pago = noches * habitacion["precio-noche"]

            nueva_reserva = {
                "id-habitacion": id_habitacion,
                "noches": noches,
                "total-pago": total_pago
            }

            reservas.append(nueva_reserva)

            print("Reserva realizada correctamente")
            print("Habitación:", habitacion["numero"])
            print("Número de noches:", noches)
            print("Total a pagar:", total_pago)

    if habitacion_encontrada == False:
        print("No existe una habitación con ese ID")


# BUSCAR LAS RESERVAS DE UNA HABITACIÓN
def buscar_reservas():

    id_habitacion = int(input("Digite el ID de la habitación: "))

    habitacion_existe = False

    for habitacion in habitaciones:
        if habitacion["id"] == id_habitacion:
            habitacion_existe = True

    if habitacion_existe == True:

        reserva_encontrada = False
        total_cobrado = 0

        print("\n--- RESERVAS DE LA HABITACIÓN ---")

        for reserva in reservas:

            if reserva["id-habitacion"] == id_habitacion:

                reserva_encontrada = True

                print("Noches:", reserva["noches"])
                print("Total pagado:", reserva["total-pago"])
                print("------------------------------")

                total_cobrado = total_cobrado + reserva["total-pago"]

        if reserva_encontrada == True:
            print("Total cobrado por la habitación:", total_cobrado)

        else:
            print("La habitación no tiene reservas")

    else:
 