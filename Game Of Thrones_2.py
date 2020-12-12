import random as r
import textwrap as t

def program_info():
    sep = "-" * 70
    game_title = "Game of Thrones v0.0.1"
    game_instructions = "Perteneces a la Guardia de la Noche."\
        " Llevas semanas andando al otro lado del muro, en una "\
        "expedición para detectar posibles salvajes. Llegas a un "\
        "poblado con 5 cabañas. Debes elegir en qué cabaña entrarás."\
        " Si está vacía podrás descansar... pero corres el riesgo de"\
        " encontrarte con un salvaje y morir..."
    print(sep)
    print(game_title)
    print(sep)
    print(t.fill(game_instructions,width=70))
    print(sep)

def game_init(total_cabins):
    values = ['enemy', 'friend', 'unoccupied']
    cabins = r.choices(values,k=total_cabins)
    print("Las cabañas son: " + str(cabins))
    return values, cabins

def enter_option(total_cabins):
    sel = -1
    while sel < 1:
        sel = int(input("Elije de 1 a " + str(total_cabins) + " la cabaña en la que entrarás: "))
        if sel < 1:
            print("No puede haber 0 o menos cabañas, melón.")
    return sel

def get_into_cabin(cabin, values, cabins):
    try:
        if cabins[int(cabin)-1] == values[0]:
            print("¡Has perdido! Un salvaje acaba de matarte.")
        else:
            print("Has podido pasar la noche muy a gusto.")
    except ValueError:
        print("Has metido una letra, momia.")
    except IndexError:
        print("Esa cabaña no existe, sólo hay" + str(len(cabins)) + " melón.")

def play():
    program_info()
    total_cabins = 5
    values, cabins = game_init(total_cabins)
    seguir = "S"
    while seguir.upper() == "S":
        cabin = enter_option(total_cabins)
        get_into_cabin(cabin, values, cabins)
        seguir = ""
        while seguir.upper() != "S" and seguir.upper() != "N":
            seguir = str(input("¿Quieres seguir jugando? (S/N): "))


if __name__ == "__main__":
    play()