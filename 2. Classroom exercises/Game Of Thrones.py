import random as r
import textwrap as t

if __name__ == "__main__":
    seguir = "S"
    sep = "-" * 70
    total_cabins = 5
    values = ['enemy', 'friend', 'unoccupied']
    cabins = r.choices(values,k=total_cabins)
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
    print("Las cabañas son: " + str(cabins))
    while seguir.upper() == "S":
        try:
            sel = int(input("Elije de 1 a " + str(total_cabins) + " la cabaña en la que entrarás: "))
            if sel > 1:
                if cabins[int(sel)-1] == values[0]:
                    print("¡Has perdido! Un salvaje acaba de matarte.")
                else:
                    print("Has podido pasar la noche muy a gusto.")
                seguir = ""
            else:
                print("Esa cabaña no existe, melón.")
                seguir = "S"
        except ValueError:
            print("Has metido una letra, momia.")
            seguir = "S"
        except IndexError:
            print("Esa cabaña no existe, melón.")
            seguir = "S"
        while seguir.upper() != "S" and seguir.upper() != "N":
            seguir = str(input("¿Quieres seguir jugando? (S/N): "))