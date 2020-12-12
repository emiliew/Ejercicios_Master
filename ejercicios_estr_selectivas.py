# 01.   Pedir la edad al usuario e indicar si es mayor de edad o no. Establecer como constante el valor de mayor de edad.
MAYORIA = 18
edad = input("Dime tu edad: ")
if int(edad) < 0:
    print("Un número negativo no es una edad.")
elif int(edad) < 18:
    print("Es menor de edad.")
else: 
    print("Es mayor de edad.")


# 02.   Crea una lista favorite_movies con los valores ‘Iron Man’, ‘Captain America’, ‘Avengers’. Pide al usuario el nombre de una película. 
#       Deberás comprobar si su película coincide con alguna de la lista. Si es así se mostrará el mensaje “A los dos nos gusta la misma película: 
#       nombre peli”. Sino coincide se mostrará el mensaje “No nos gustan las mismas películas.
favorite_movies = ["Iron Man", "Captain America", "Avengers"]
chosen_movie = input("Dime el nombre de una película: ")
if chosen_movie in favorite_movies:
    print("A los dos nos gusta la misma película.")
else:
    print("No nos gustan las mismas películas.")
# 03.   ¿Qué sucede si la película que escribe el usuario está en minúsculas o mayúculas? Depura el programa para que coincida con los textos 
#       escritos en la lista
favorite_movies = ["Iron Man", "Captain America", "Avengers"]
chosen_movie = input("Dime el nombre de una película: ")
print("Película elegida: "+chosen_movie.lower().capitalize())
if chosen_movie.lower().capitalize() in favorite_movies:
    print("A los dos nos gusta la misma película.")
else:
    print("No nos gustan las mismas películas.")
# 04.   La entrada a un museo dependerá de la edad del visitante. Si es menor de 4 años el acceso será gratuito, hasta 12 años pagará 4,5€, a partir 
#       de 12 años será como un adulto y la entrada será 8€. Realiza un programa en Python que solicite la edad al visitante y le calcule el precio 
#       de la entrada.
# 05.   Solicitar la edad al usuario y en función de esta le mostraremos un mensaje:
#           a. Menores de 2 años: “¡Eres un bebe!”
#           b. Menores de 4 años: “¡Eres un crí@!”
#           c. Menores de 13 años: “¡Eres un niñ@!”
#           d. Menores de 20 años:”¡Eres un adolescente”!
#           e. Menores de 65: “¡Eres adulto!”
#           f. Resto: “Eres un ancian@”
# 06.   Escribe del 1 al 9 la siguiente salida, utilizando un bucle for y if-elif-else
#           1st
#           2nd
#           3rd
#           4th
#           5th
#           6th
#           7th
#           8th
#           9th