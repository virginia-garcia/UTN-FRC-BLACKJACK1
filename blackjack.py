# funcion validadora
def validate(minim, maxi, val):
    # validar que el nro(val) sea menor al max y mayor al min
    while maxi < val < minim:
        # si es menor al min muestra el msj y lo hace ingresar de nuevo
        if val < minim:
            val = int(input('ERROR!!!, Ingrese un valor mayor a ' + str(minim) + ':'))
        # Si es menor al min muestra el msj y lo hace ingresar de nuevo
        if maxi < val:
            val = int(input('ERROR!!!, Ingrese un valor menor a ' + str(maxi) + ':'))
    return val


# funcion de apuesta
def apuesta(monto, pozo):
    while pozo > 100000:
        pozo = int(input('Ingrese el monto del pozo '))
    while pozo <= 100000:
        monto = int(input('Defina el monto a apostar: '))
        print("El pozo es de: ", pozo)
        if monto % 5 == 0 and monto <= pozo:
            print("La apuesta es de: ", monto)
            break
        else:
            print('\nAposto un monto que no cumple con los requisitos. Vuelva a intentar.')
    return monto, pozo


# función de dar cartas y mostrarlas
def mano(a, b):
    num = random.choice(a)
    palo = random.choice(b)
    print("La carta es un", num, "de", palo)
    if num == "J" or num == "Q" or num == "K":
        num = 10
    elif num == "A":
        num = 11
    return num


# funcion comparar para saber quien gano, perdio o empataron. Usamos como parametros el monto, pozo, acumulador
# de puntos del jugador y del crupier. Esta funcion retornara los valores para saber quien gano, cuanto perdio el
# jugador y el pozo para que se vaya actualizando.

def comparar(monto, pozo, acumcarta, acumcrupier):
    perdiojugador = 0
    banderagano = None

    if acumcrupier == acumcarta and acumcarta < 22 and acumcrupier < 22:
        print("El jugador y el crupier empataron con ", acumcarta, "puntos.")
        print("El monto actulizado es: ", pozo)
        banderagano = None
        perdiojugador = 0

    if acumcrupier < acumcarta < 22 and acumcrupier < 22:
        print("El jugador gano con : ", acumcarta, "puntos.")
        pozo += monto
        print("El monto actulizado es: ", pozo)
        banderagano = True
        perdiojugador = 0

    if acumcarta < acumcrupier < 22 and acumcarta < 22:
        print("El crupier gano con ", acumcrupier, "puntos.")
        pozo -= monto
        print("El monto actulizado es: ", pozo)
        banderagano = False
        perdiojugador = monto

    if acumcrupier > 22 and acumcarta > 22:
        print("El crupier y el jugaror perideron. Pero termina ganando el crupier")
        pozo -= monto
        print("El monto actulizado es: ", pozo)
        banderagano = False
        perdiojugador = monto

    return banderagano, perdiojugador, pozo


def opcion1(pozo):
    # debe actualizar el valor del pozo verificando que no sea 0 o negativo (x > 0)
    agregar = int(input("¿Desea agregar mas dinero al monto? (si = 1)(no = 0): "))
    if agregar == 1:
        pozomas = int(input("Dinero a agregar al pozo: "))
        if pozomas > 0:
            if pozo + pozomas <= 100000:
                pozo += pozomas
                print("Su nuevo pozo es de: ", pozo)
                return pozo
            else:
                print(
                    "Valor incorrecto, el valor total del poso debe ser menor a $100.000\nvuelva a ingresar a la opcion.")
    return pozo


def opcion2(pozo, monto=None):
    # debe retornar si ganó el jugador o el crupier, si hubo blackjack natural en la mano y cuanto perdió el jugador si perdió
    # Funciones dispoibles:
    #   ases(), validate(), mano(), valid_21() ... ver para qeu sirve cada función en su descripción

    # En cada mano se debe mostrar:
    # 1 Monto inicial del pozo (previo a la apuesta).
    # 2 Monto de la apuesta.
    # 3 Cartas de cada jugador y su puntaje final.
    # 4 Mensaje indicando quién es el ganador.
    # 5 Monto actualizado del pozo.

    # declarar las variables

    banderaAS1 = banderaAS2 = banderagano = bandera3 = bandera4 = bandera5 = bandera6 = bandera7 = False
    acumcarta = acumcuprier = cont11 = perdiojugador = 0
    a = 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A'
    b = 'pica', 'corazón', 'diamante', 'trébol'

    monto, pozo = apuesta(monto, pozo)

    # primer carta al cuprier
    print("\n - - - - - Primera carta del cuprier - - - - -")
    cartacuprier = mano(a, b)
    acumcuprier += cartacuprier
    # aca generamos una vandera para que cuando salgan dos 11, el segunto trabaje con valor de "1"
    if cartacuprier == 11:
        banderaAS2 = True

    # primeras 2 cartas al jugador
    print("\n - - - Primera y segunda carta del jugador - - -")
    for i in range(2):
        carta = mano(a, b)
        if carta == 11:
            cont11 += 1
            banderaAS1 = True
            if cont11 == 1:
                acumcarta += carta
            if cont11 == 2:
                banderaAS1 = True
                acumcarta = 12
        else:
            acumcarta += carta
    print("\tEl valor de la suma de las dos cartas es: ", acumcarta)

    # si quiere mas manos
    # si desea otra carta ingrese el numero "1", de lo contrario ingrese "0".
    while acumcarta < 21:
        x = int(input("Quiere otra carta mas? (1 = si o  0 = no): "))
        if x == 1:
            carta3 = mano(a, b)
            if banderaAS1:
                if carta3 == 11:
                    carta3 = 1
                    acumcarta += carta3
                else:
                    acumcarta += carta3
            else:
                acumcarta += carta3

            print("\nEl valor de la suma de las cartas es: ", acumcarta)
            if acumcarta > 21:
                print("\nEl jugador se paso con, ", acumcarta, " puntos.")
                bandera6 = True
                perdiojugador = monto
            elif acumcarta == 21:
                print("El jugador gano, realizo black jack.")
                bandera4 = True
                pozo += monto
                print("El monto actulizado es: ", pozo)
                break
        else:
            if x == 0:
                print("El jugador se planta con", acumcarta)
                break
    else:
        if acumcarta == 21:
            print("El jugador gano haciendo black jack natural")
            bandera4 = True
            pozo += monto
            print("El monto actulizado es: ", pozo)

    # si el jugador saco blackyac no juega el crupier
    if bandera4:
        print("\nFinalizo el juego\n")
    else:
        # manos del cuprier
        print("\n - - - Manos carta del crupier - - -")
        while acumcuprier <= 16:
            cartacuprier = mano(a, b)
            if banderaAS2:
                if cartacuprier == 11:
                    cartacuprier = 1
                    acumcuprier += cartacuprier
                else:
                    acumcuprier += cartacuprier
                if cartacuprier == 10:
                    print("El crupier gano haciendo black jack natural")
                    pozo -= monto
                    print("El monto actulizado es: ", pozo)
                    bandera4 = True
            else:
                if cartacuprier == 11:
                    banderaAS2 = True
                    acumcuprier += cartacuprier
                    if acumcuprier == 21:
                        print("El crupier gano haciendo black jack natural")
                        pozo -= monto
                        print("El monto actulizado es: ", pozo)
                        bandera4 = True

                else:
                    acumcuprier += cartacuprier
        else:
            if bandera4:
                pass
            else:
                if 22 > acumcuprier > 16:
                    print("El cuprier se planta con ", acumcuprier, "puntos.")
                    if bandera6:
                        print("\nEl cuprier gano, con", acumcuprier, ". Porque se paso el jugador")
                        pozo -= monto
                        banderagano = False
                        perdiojugador = monto
                        print("El monto actulizado es: ", pozo)
                        bandera7 = True
                if acumcuprier == 21:
                    print("\nEl cuprier gano, realizo black jack")
                    bandera5 = True
                    pozo -= monto
                    perdiojugador = monto
                    print("El monto actulizado es: ", pozo)
                    banderagano = False
                else:
                    if acumcuprier > 21:
                        print("\nEl cuprier se paso con", acumcuprier, "puntos.")
                        if acumcarta < 22:
                            print("\nEl jugador gano con", acumcarta)
                            bandera3 = True
                            pozo += monto
                            banderagano = True
                            print("El monto actulizado es: ", pozo)
                        else:
                            print("\nEl cuprier y el jugador se pasaron con los puntos. Gana el crupier por regla")
                            pozo -= monto
                            perdiojugador = monto

                            print("El monto actulizado es: ", pozo)
                            banderagano = False

    # vanderas para black jack o cuando el crupier se pasa.
    if bandera4:
        print()
    else:
        if bandera3 or bandera5 or bandera6 or bandera7:
            print("\n\t\tFinalizo el juego")
        else:
            banderagano, perdiojugador, pozo = comparar(monto, pozo, acumcarta, acumcuprier)

    return bandera4, banderagano, perdiojugador, pozo


def opcion3(cant_part=0, cant_vic=0, rach=0, cant_nat=0, max_poso=0, prom_ap=0, may_perd=0):
    # Esta funci�n se encarga de mostrar en pantalla los datos finales:
    # El porcentaje de victorias del jugador.
    # La racha m�s larga de victorias del croupier.
    # La cantidad de manos donde hubo un blackjack natural
    # El monto m�ximo que lleg� a tener el jugador en el pozo.
    # El monto promedio del que dispuso el jugador para realizar apuestas.
    # La p�rdida m�s grande que sufri� el jugador (si hubo alguna)
    porc_jugador = round(cant_vic * 100 / cant_part, 1)
    promedio_ap = round(prom_ap / cant_part)
    print('\nResultados finales:\n')
    print('\tEl porcentaje de victorias del jugador sobre el total de manos es del ' + str(porc_jugador) + '%')
    print('\tLa racha de victorias del crupier es de', rach, 'manos')
    print('\tHubo', cant_nat, 'de manos en donde hubo blackjack natural (21 con 2 cartas)')
    print('\tEl monto m�ximo que lleg� a tener el jugador es de $' + str(max_poso))
    print('\tEl promedio del que dispuso el jugador para apostar es de $', str(promedio_ap))
    print('\tLa mayor p�rdida del jugador fu� de $' + str(may_perd))


def menu(pozo):
    # se necesita un contador para la cantidad de manos jugadas, la cantidad de victorias del jugador
    # un acumulador para contar la racha mas larga del crupier (se reset�a cada vez que el crupier pierde)
    # una variable para guardar el monto mas grande en el poso hasta el final, y otra para la p�rdida mas grande del
    # jugador en todas las amnos
    cant_man = gan_jugad = rach_crup = may_poso = cant_vein = pos_tot = max_cuant = max_rach_cr = 0

    opcion = -1
    while opcion != 3:
        opcion = int(
            input('\n\n\t\t\tJUEGO DE BLACKJACK \n\n1- Apostar \n2- Jugar una Mano \n3- Salir\n\n \nElija su opción: '))
        validate(1, 3, opcion)
        if opcion == 1:
            pozo = opcion1(pozo)
        elif opcion == 2:
            # nat = cant de Black jack natural. quien = quien gano. cuan = cuanto dinero perdio el jugador apostando.
            nat, quien, cuan, pozo = opcion2(pozo)

            cant_man += 1
            pos_tot += pozo
            if quien:
                gan_jugad += 1
                if max_rach_cr < rach_crup:
                    max_rach_cr = rach_crup
                rach_crup = 0

            elif not quien:
                if max_rach_cr < rach_crup:
                    max_rach_cr = rach_crup
                rach_crup += 1

            elif quien is None:
                if max_rach_cr < rach_crup:
                    max_rach_cr = rach_crup
                rach_crup = 0

            if may_poso < pozo:
                may_poso = pozo

            if nat:
                cant_vein += 1

            if max_cuant < cuan:
                max_cuant = cuan

        elif opcion == 3:
            opcion3(cant_man, gan_jugad, max_rach_cr, cant_vein, may_poso, pos_tot, max_cuant)


def test():
    pozo = float(input('Ingrese el valor inicial del pozo: '))
    nomb = input('Ingrese su nombre: ')

    menu(pozo)

    print('Gracias por utilizar el programa,', nomb)


if __name__ == '__main__':
    test()
