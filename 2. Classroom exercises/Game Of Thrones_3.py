import random as r

def program_info():
    """Esta función muestra el título y las instrucciones del juego.
    """

    sep = "-" * 70
    game_title = "Game of Thrones v0.0.1"
    game_instructions = "Perteneces a la Guardia de la Noche. Llevas semanas andando al otro lado del muro, en una expedición para \n"\
                        "detectar posibles salvajes. Llegas a un poblado con 5 cabañas. Debes elegir en qué cabaña entrarás. Si \n"\
                        "está vacía podrás descansar... pero corres el riesgo de encontrarte con un salvaje y morir...\n"
    game_instructions2 = "Recuerda las siguientes reglas:\n"\
                            "- Si visitas una cabaña y encuentras a un enemigo tendrás que luchar a muerte o huir y morir.\n"\
                            "- Si llegas a una cabaña ocupada por un compañero podrás conseguir un arma que mejore tu poder de ataque.\n"\
                            "- Si alcanzas una cabaña vacía podrás descansar y recuperar toda la vida.\n"\
                            "- No puedes visitar más de una vez la misma cabaña.\n"\
                            "- Puedes abandonar el juego en cualquier momento, pero visitando todas las cabañas podrás ganar la partida.\n"
    print(sep)
    print(game_title)
    print(sep)
    print(game_instructions)
    print(game_instructions2)
    print(sep)

def game_init(total_cabins):
    """Esta función inicializa los valores de todas las variables
    del juego.

    Args:
        total_cabins (int):             Nº de cabañas en el juego.

    Returns:
        tupl(str):                      Valores que puede tener cada cabaña (enemigo, amigo o desocupada)
        list[str]:                      Valores que tiene cada cabaña.
        dict{int:bool}:                 Diccionario con número de cabaña y si se ha visitado (True) o no (False). 
        dict{str:int}:                  Diccionario con la cantidad de vida del jugador y de enemigo/s.
        dict{str:list}:                 Diccionario con armas del juego y rangos de daño
        list[str]:                      Lista cuyo primer elemento contiene el arma equipada para poder pasar por referencia.
    """
    hp = {"player": 50, "enemy":0} # la salud del enemigo se reseteará en cada cabaña enemiga, la del jugador sólo cuando descansa.
    visited_cabins = dict((i, False) for i in range(1, total_cabins+1))    
    values_cabin = ['enemy', 'friend', 'unoccupied']
    weapon_equip = [""]
    cabins = r.choices(values_cabin,k=total_cabins)
    weapons_game = {"Cuchillo":range(15,20), "Espada":range(20,26), "Bazooka":range(30,41)}
    # print(weapons_game) --------------------------- Para mostrar las armas en el testing.
    # print("Las cabañas son: " + str(cabins)) ------ Para mostrar las cabañas en el testing.
    return values_cabin, cabins, visited_cabins, hp, weapons_game, weapon_equip

def enter_option(total_cabins):
    """Esta función recoge la opción que el jugador quiere introducir.

    Args:
        total_cabins (int):             Número de opciones (cabañas) disponibles

    Returns:
        int :                           Opción elegida
    """
    sel = -1
    while sel < 1:
        sel = int(input("Elije de 1 a " + str(total_cabins) + " la cabaña en la que entrarás: "))
        if sel < 1:
            print("No puede haber 0 o menos cabañas, melón.")
    return sel

def get_into_cabin(cabin_chosen, values_cabin, cabins, visited_cabins, hp, weapons_game, weapon_equip):
    """Esta función introduce al jugador en la cabaña y contiene la lógica de juego.

    Args:
        cabin (int):                    Opción (cabaña) elegida por el jugador
        values (tupl(str)):             Valores que puede tener cada cabaña
        cabins (list[str]):             Valores que tiene cada cabaña
        visited (dict{int:bool}):       Diccionario con número de cabaña y si se ha visitado o no
        hp (dict{str:int}):             Diccionario con la cantidad de vida del jugador y de enemigo/s
        weapons_game (dict{str:list}):  Diccionario con armas del juego y rangos de daño
        weapon_equip (list[str]):       Lista cuyo primer elemento contiene el arma equipada para poder pasar por referencia.
    """
    
    print("Entrando a la cabaña nº "+str(cabin_chosen))
    if visited_cabins[cabin_chosen] == False:
        visited_cabins[cabin_chosen] = True # introduzco la cabaña en el diccionario de visitadas.
        if cabins[int(cabin_chosen)-1] == values_cabin[0]:
            print("¡Un malo!")
            hp["enemy"] = 40
            luchar = ""
            while str(luchar).upper() != "N" and hp["player"] > 0 and hp["enemy"] > 0:
                luchar = input("¿Deseas atacar? (S/N): ")
                if luchar.upper() == "S":
                    lucha(hp, weapons_game, weapon_equip)
                    if(hp["enemy"] <= 0): # enemigo muerto
                        print('¡Has vencido al salvaje!')
                    elif(hp["player"] <= 0): # jugador muerto
                        print("¡Te han pelado el culo!")
                elif luchar.upper() == "N": # jugador se rinde
                    print("Eliges huir. Pierdes cual gallina.")
                    hp["player"] = 0
        elif cabins[int(cabin_chosen)-1] == values_cabin[1]:
                print("Llegas a una cabaña y te encuentras con otro guardián de la noche.")
                arma_encontrada = encuentra(weapons_game)
                if arma_encontrada != "":
                    print("Tu compañero te ofrece el arma " + arma_encontrada + " que hace de " + str(min(weapons_game[arma_encontrada])) + " a " + str(max(weapons_game[arma_encontrada])) + " de daño.")
                    if weapon_equip[0] == "":
                        print("Hasta ahora no tenías ningún arma, así que guardas el arma " + arma_encontrada + " en tu fardo.")
                    elif arma_encontrada == weapon_equip[0]:
                        print("Ya tienes una igualita.")
                    elif max(list(weapons_game[weapon_equip[0]])) > max(list(weapons_game[arma_encontrada])):
                        print("Ahora mismo tienes el arma " + weapon_equip + ", que es mucho más potente.")
                    else:
                        print("El arma " + arma_encontrada + " es mejor que tu " + weapon_equip + ", así que la guardas en tu fardo.")
                        weapon_equip[0] = arma_encontrada
                else:
                    print("Tu compañero no tiene nada para ti, sólo conversación. No has podido descansar nada.")
        else:
            print("Encuentras una cabaña vacía y tranquila. Has podido pasar la noche muy a gusto. ¡Recuperas todos los puntos de vida!")
            hp["player"] = 50
        print_hp(hp) # Imprimo los puntos de vida al salir.
    else:
        print("Ya has visitado esta cabaña, inténtalo con otra.")

def encuentra(armas):
    arma = ""
    if r.randint(1, 2) == 1:
        arma = r.choice(list(armas.keys()))
    return arma

def lucha(hp, armas, arma_equip):
    """Método que simula la lucha

    Args:
        hp (dict{str:int}):             Puntos de vida
        weapons_game (dict{str:list}):  Diccionario con armas del juego y rangos de daño
        weapon_equip (list[str]):       Lista cuyo primer elemento contiene el arma equipada para poder pasar por referencia.           

    """
    print("¡ATAQUE!")
    damage = r.randrange(10,16) # Calculo el daño aleatorio de 10 a 15:
    prob = r.randrange(10) # Calculo un número aleatorio del 0 al 9
    if(prob<6): # Si el número calculado va de 0 a 5, golpea el jugador:
        if arma_equip[0] != "":
            damage = r.choice(list(armas[arma_equip[0]]))
        print("Golpeas al enemigo haciéndole "+str(damage)+" de daño.")
        hp["enemy"] -= int(damage)
    else: # Si el número va de 6 a 9, golpea el enemigo:
        print("El enemigo te mete un collejón haciéndote "+str(damage) +" de daño.")
        hp["player"] -= int(damage)
    print_hp(hp)

def print_hp(hp):
    """Imprime la puntuación de jugador y enemigo.

    Args:
        hp (dict{str:int}): Puntos de vida de jugador y enemigo.
    """
    if hp["enemy"] <= 0:
        print("Health: Night Wachtman: "+str(hp["player"]))
    else:
        print("Health: Night Wachtman: "+str(hp["player"])+", Wild: "+str(hp["enemy"]))

def print_cabins(visited_cabins, cabins):
    print(list(visited_cabins.values()).count(True))
    if list(visited_cabins.values()).count(True) != 0:
        print("De las " + str(len(cabins)) + " has visitado las siguientes:")
        print([str(i) for i in range(1, len(cabins)+1) if visited_cabins[i]==True])
    else:
        print("Aún no has visitado ninguna de las " + str(len(cabins)) + " cabañas.")

def play():
    program_info()
    total_cabins = 5
    values_cabin, cabins, visited_cabins, hp, weapons_game, weapon_equip = game_init(total_cabins)
    seguir = "S"
    while seguir.upper() == "S" and hp["player"] > 0:
        print_cabins(visited_cabins, cabins)
        try:
            cabin = enter_option(total_cabins) # Pedimos nº de cabaña.
            get_into_cabin(cabin, values_cabin, cabins, visited_cabins, hp, weapons_game, weapon_equip) # Entramos en  cabaña.
            if hp["player"] > 0: # Tras salir de la cabaña, comprobamos si el jugador sigue vivo.
                if list(visited_cabins.values()).count(False) == 0: # Si sigue vivo y ha visitado todas las cabañas, ha ganado. Fin.
                    print("WOW chaval, has logrado visitar todas las cabañas y sigues vivo. ¡ENHORABUENA!")
                    seguir = "N"
                else: # Si sigue vivo pero no ha visitado todas las cabañas, preguntamos si quiere seguir.
                    seguir = "" 
                    while seguir.upper() != "S" and seguir.upper() != "N":
                        seguir = str(input("¿Quieres seguir jugando? (S/N): "))
            else:
                seguir = "N"
        except ValueError:
            print("Has metido una letra, momia.")
        except IndexError:
            print("Esa cabaña no existe, sólo hay " + str(len(cabins)) + ", melón.")
    print("Fin de partida.") # El jugador ha muerto o ha ganado la partida.


if __name__ == "__main__":
    play()