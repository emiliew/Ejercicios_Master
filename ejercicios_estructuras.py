# LISTAS:
print("\n------------LISTAS------------\n") 


# 01: Crea una lista llamada bicycles con los valores ‘trek’, 
# ‘cannondale’,’redline’, ‘specialized’. Muestra por pantalla 
# los valores de la lista
print("\n- Ejercicio 1-1:")
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# 02: Muestra por pantalla el segundo elemento de la lista bicycles. 
# ¿En qué posición comienzan las listas Python?
print("\n- Ejercicio 1-2:")
print(bicycles[1])

# 03: Muestra el segundo elemento de la lista bicycles teniendo en 
# cuenta que la primera letra sea mayúsculas. Es decir, mostrar: Cannondale
print("\n- Ejercicio 1-3:")
print(bicycles[1].capitalize())

# 04: Mostrar el último elemento de la lista, teniendo en cuenta que 
# desconocemos el número de elementos que tiene. Es decir, mostrar specialized
print("\n- Ejercicio 1-4:")
print(bicycles[len(bicycles)-1])

# 05: Mostrar por pantalla el siguiente mensaje “My first bicycle was a Trek.”
print("\n- Ejercicio 1-5:")
print("My first bicycle was a Trek.")

# 06: Crea una lista llamada motorcycles con los valores ‘honda’, ‘yamaha’, 
# ‘suzuki’. A continuación, mostrar por pantalla la lista
print("\n- Ejercicio 1-6:")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# 07: ¿Qué sucede si se asigna en la posición 0 de la lista motorcycle el 
# valor ‘ducati’?
print("\n- Ejercicio 1-7:")
motorcycles[0] = "ducati"
print(motorcycles[0])

# 08: Añade al final de la lista motorcycle el valor ‘honda’. Muestra por 
# pantalla la lista.
print("\n- Ejercicio 1-8:")
motorcycles.append("honda")
print(motorcycles)

# 09: Elimina el elemento 0 de la lista motorcycle. Muestra la lista.
print("\n- Ejercicio 1-9:")
motorcycles.remove(motorcycles[0])
print(motorcycles)

# 10: Inserta en la primera posición de la lista motorcycle el valor ‘ducati’. 
# Muestra la lista
print("\n- Ejercicio 1-10:")
motorcycles.insert(0, "ducati")
print(motorcycles)

# 11: De la lista motorcycles elimina el último elemento y quédate con él en una 
# nueva variable llamada motorcycles_popped. Comprueba el tipo de esta variable.
print("\n- Ejercicio 1-11:")
motorcycles_popped = motorcycles.pop(len(motorcycles)-1)
print(motorcycles)
print(motorcycles_popped)
print(type(motorcycles_popped))

# 12: Elimina de la lista motorcycles el elemento ‘yamaha’. Muestra por pantalla 
# la lista.
print("\n- Ejercicio 1-12:")
motorcycles.remove("yamaha")
print(motorcycles)

# 13: Vuelve a crear la lista motorcycles pero en esta ocasión vacía. Es decir 
# motocycles=[] A continuación, añade los valores ‘yamaha’, ‘ducati’, ‘suzuki’, 
# ‘ducati’, ‘ducati’. Elimina el valor ‘ducati’. Muestra la lista
print("\n- Ejercicio 1-13:")
motorcycles = []
motorcycles.append("yamaha")
motorcycles.append("ducati")
motorcycles.append("suzuki")
motorcycles.append("ducati")
motorcycles.append("ducati")
motorcycles.remove("ducati")
print(motorcycles)

# 14: Vamos a reiniciar la lista motorcycles con los valores ‘yamaha’, ‘suzuki’,’honda’,
# ’ducati’. A continuación, ordena la lista y muestrala.
print("\n- Ejercicio 1-14:")
motorcycles = ["yamaha", "suzuki", "honda", "ducati"]
motorcycles.sort()
print(motorcycles)

# 15: ¿De qué manera podríamos tener la lista original de motocycles sin ordenar y 
# ordenada? Prueba con sorted
print("\n- Ejercicio 1-15:")
motorcycles = ["yamaha", "suzuki", "honda", "ducati"]
print(motorcycles)
print(sorted(motorcycles))

# 16: ¿Cuántos elementos tiene la lista motorcycles?
print("\n- Ejercicio 1-16:")
print("La lista motorcycles tiene " + str(len(motorcycles)) + " elementos")

# 17: Imprime los elementos de la lista de inicio a fin y luego al revés.
print("\n- Ejercicio 1-17:")
print("\nDe inicio a fin:")
print(motorcycles)
print("\nAl revés:")
motorcycles.reverse()
print(motorcycles)

# 18: ¿Qué sucede si intentas mostrar por pantalla a motocycles[4]? ¿Por qué?
print("\n- Ejercicio 1-18:")
try:
    print(motorcycles[4])
except Exception as e:
    print(e)

# 19: ¿Qué imprimes si accedes a motorcycles[-1]?
print("\n- Ejercicio 1-19:")
print(motorcycles[-1])

# 20: A continuación, vamos a quedarnos con una slice (usando rangos) de la lista 
# motorcycles.Nos quedaremos con los valores ‘honda’ y ‘suzuki’. Muéstralo por pantalla.
print("\n- Ejercicio 1-20:")
slice = motorcycles[1:3]
print(slice)

# 21: A continuación, nos quedaremos desde el segundo elemento hasta el final. Mostrar 
# por pantalla.
print("\n- Ejercicio 1-21:")
slice = motorcycles[1:]
print(slice)

# 22: Vamos a crear dos listas. La lista my_foods con los valores ‘pizza’, ‘cakes’, ‘meat’. 
# La otra lista la crearemos como una copia de my_foods y la llamaremos family_foods. 
# A continuación, mostrar los mensajes:
#   a. My favorite foods are: seguido de my_foods
#   b. My family’s favorite foods are: seguido de family_foods
print("\n- Ejercicio 1-22:")
my_foods = ["pizza", "cakes", "meat"]
family_foods = my_foods[:]
print("My favorite foods are: " + str(my_foods))
print("My family's favorite foods are: " + str(family_foods))

# 23: Añadir a my_foods el valor ‘ice cream’. Imprimir las listas my_foods y family_foods.
print("\n- Ejercicio 1-23:")
my_foods.append("ice cream")
print("My favorite foods are: " + str(my_foods))
print("My family's favorite foods are: " + str(family_foods))

# 24: Crea un programa en Python que tenga dos listas vowels con las vocales y found con 
# las vocales que se encuentren en una palabra que se solicite al usuario. Mostrar el 
# contenido de found
print("\n- Ejercicio 1-24:")
vowels = ["a","e","i","o","u"]
found = []
#frase = input("Introduzca una frase para contar sus vocales: ")
#for vowel in vowels:
    #print("Hay " + str(frase.count(vowel))+ " " + vowel + " en tu frase.")

# TUPLAS:
print("\n------------TUPLAS------------\n") 

# 01: Crea la tupla dimensions con los valores 100 y 200. Muestra por pantalla la tupla 
# y su tipo
print("\n- Ejercicio 2-1:")
dimensions = (100, 200)
print(dimensions)
print(type(dimensions))

# 02: Muestra por pantalla el primer elemento de la tupla y su tipo
print("\n- Ejercicio 2-2:")
print(dimensions[0])
print(type(dimensions[0]))

# 03: Muestra todos los elementos de la tupla. Utiliza un bucle.
print("\n- Ejercicio 2-3:")
for d in dimensions:
    print(d)

# DICCIONARIOS:
print("\n------------DICCIONARIOS------------\n")

# 01:Solicita al usuario su nombre, dirección, edad, teléfono y guárdalo en un diccionario
# person. A continuación, muestra por pantalla el texto: <nombre> tiene <edad> años, vive en 
# <dirección> y su número de teléfono es <teléfono>
# 02: Crea un diccionario vacio persony rellénalo con la información de una persona. Para 
# ello, será consultando al usuario el dato que quiere guardar y el valor.
""" print("\n- Ejercicio 3-1 / 3-2:")
person = {"Nombre":None,"Edad":None,"Dirección":None,"Teléfono":None}
repeat1 = True
while(repeat1):
    repeat2 = True
    key_u = input("¿Qué dato quieres añadir?: ")
    if (list(person.keys()).count(key_u)):
        person[key_u] = input("¿Qué valor quieres introducir para " + key_u +"?: ")
        while(repeat2):
            answer = input("Quieres añadir más información (S/N)?: ")
            if(answer == "S"): 
                repeat2 = False
            elif(answer == "N"):
                repeat1 = False
                repeat2 = False
                print("Programa finalizado.")
            else:
                print("Respuesta no conocida.")
    else print("Clave no reconocida. Pruebe de nuevo.")
print("Resultado:")
print(str(person["Nombre"]) + " tiene " + str(person["Edad"]) + " años, vive en " 
    + str(person["Dirección"]) + " y su número de teléfono es " + str(person["Teléfono"])) """

# 03: Crea un diccionario(currences) que contenga el nombre de los países y su moneda. A 
# continuación, mostrar los países que tiene el diccionario y solicitar al usuario escriba 
# alguno de esos países para mostrarle la moneda

currencies = {"Afghanistan":"Afghanistan Afghani","Albania":"Albanian Lek","Algeria":"Algerian Dinar",
    "Andorra":"Euro","Angola":"Angolan Kwanza","Argentina":"Argentine Peso",
    "Armenia":"Armenian Dram","Australia":"Australian Dollar","Austria":"Euro",
    "Azerbaijan":"Azerbaijan New Manat","Belarus":"Belarussian Ruble","Belgium":"Euro",
    "Bolivia":"Boliviano","Bosnia-Herzegovina":"Marka","Botswana":"Botswana Pula",
    "Bulgaria":"Bulgarian Lev","Cambodia":"Kampuchean Riel","Cameroon":"CFA Franc BEAC",
    "Canada":"Canadian Dollar","Cape Verde":"Cape Verde Escudo",
    "Central African Republic":"CFA Franc BEAC","Chile":"Chilean Peso","China":"Yuan Renminbi",
    "Colombia":"Colombian Peso","Congo":"CFA Franc BEAC","Congo, Dem. Republic":"Francs",
    "Costa Rica":"Costa Rican Colon","Croatia":"Croatian Kuna","Cuba":"Cuban Peso","Cyprus":"Euro",
    "Czech Rep.":"Czech Koruna","Denmark":"Danish Krone","Dominican Republic":"Dominican Peso",
    "Ecuador":"Ecuador Sucre","Egypt":"Egyptian Pound","El Salvador":"El Salvador Colon",
    "Estonia":"Euro","Ethiopia":"Ethiopian Birr","European Union":"Euro","Finland":"Euro",
    "France":"Euro","Gabon":"CFA Franc BEAC","Gambia":"Gambian Dalasi","Georgia":"Georgian Lari",
    "Germany":"Euro","Ghana":"Ghanaian Cedi","Gibraltar":"Gibraltar Pound",
    "Great Britain":"Pound Sterling","Greece":"Euro","Greenland":"Danish Krone",
    "Guatemala":"Guatemalan Quetzal","Haiti":"Haitian Gourde","Honduras":"Honduran Lempira",
    "Hong Kong":"Hong Kong Dollar","Hungary":"Hungarian Forint","Iceland":"Iceland Krona",
    "India":"Indian Rupee","Indonesia":"Indonesian Rupiah","Iran":"Iranian Rial",
    "Iraq":"Iraqi Dinar","Ireland":"Euro","Israel":"Israeli New Shekel","Italy":"Euro",
    "Ivory Coast":"CFA Franc BCEAO","Jamaica":"Jamaican Dollar","Japan":"Japanese Yen",
    "Jordan":"Jordanian Dinar","Kazakhstan":"Kazakhstan Tenge","Kenya":"Kenyan Shilling",
    "Kuwait":"Kuwaiti Dinar","Laos":"Lao Kip","Latvia":"Latvian Lats","Lebanon":"Lebanese Pound",
    "Lesotho":"Lesotho Loti","Liberia":"Liberian Dollar","Libya":"Libyan Dinar",
    "Liechtenstein":"Swiss Franc","Lithuania":"Lithuanian Litas","Luxembourg":"Euro",
    "Macau":"Macau Pataca","Macedonia":"Denar","Madagascar":"Malagasy Franc",
    "Malawi":"Malawi Kwacha","Malaysia":"Malaysian Ringgit","Maldives":"Maldive Rufiyaa",
    "Mali":"CFA Franc BCEAO","Malta":"Euro","Mauritania":"Mauritanian Ouguiya",
    "Mexico":"Mexican Nuevo Peso","Micronesia":"US Dollar","Moldova":"Moldovan Leu",
    "Monaco":"Euro","Mongolia":"Mongolian Tugrik","Montenegro":"Euro",
    "Morocco":"Moroccan Dirham","Mozambique":"Mozambique Metical","Myanmar":"Myanmar Kyat",
    "Namibia":"Namibian Dollar","Nauru":"Australian Dollar","Nepal":"Nepalese Rupee",
    "Netherlands":"Euro","New Zealand":"New Zealand Dollar","Nicaragua":"Nicaraguan Cordoba Oro",
    "Niger":"CFA Franc BCEAO","Nigeria":"Nigerian Naira","North Korea":"North Korean Won",
    "Norway":"Norwegian Krone","Oman":"Omani Rial","Pakistan":"Pakistan Rupee",
    "Palau":"US Dollar","Panama":"Panamanian Balboa","Papua New Guinea":"Papua New Guinea Kina",
    "Paraguay":"Paraguay Guarani","Peru":"Peruvian Nuevo Sol","Philippines":"Philippine Peso",
    "Poland":"Polish Zloty","Polynesia (French)":"CFP Franc","Portugal":"Euro",
    "Puerto Rico":"US Dollar","Qatar":"Qatari Rial","Romania":"Romanian New Leu",
    "Russia":"Russian Ruble","Rwanda":"Rwanda Franc","Samoa":"Samoan Tala","San Marino":"Euro",
    "Saudi Arabia":"Saudi Riyal","Senegal":"CFA Franc BCEAO","Serbia":"Dinar",
    "Sierra Leone":"Sierra Leone Leone","Singapore":"Singapore Dollar","Slovakia":"Euro",
    "Slovenia":"Euro","Somalia":"Somali Shilling","South Africa":"South African Rand",
    "South Korea":"Korean Won","South Sudan":"South Sudan Pound","Spain":"Euro",
    "Sri Lanka":"Sri Lanka Rupee","Sudan":"Sudanese Pound","Suriname":"Surinam Dollar",
    "Swaziland":"Swaziland Lilangeni","Sweden":"Swedish Krona","Switzerland":"Swiss Franc",
    "Syria":"Syrian Pound","Taiwan":"Taiwan Dollar","Tajikistan":"Tajik Somoni",
    "Tanzania":"Tanzanian Shilling","Thailand":"Thai Baht","Togo":"CFA Franc BCEAO",
    "Tunisia":"Tunisian Dollar","Turkey":"Turkish Lira","Turkmenistan":"Manat",
    "U.K.":"Pound Sterling","Uganda":"Uganda Shilling","Ukraine":"Ukraine Hryvnia",
    "United Arab Emirates":"Arab Emirates Dirham","Uruguay":"Uruguayan Peso",
    "USA":"US Dollar","Uzbekistan":"Uzbekistan Sum","Vatican":"Euro",
    "Venezuela":"Venezuelan Bolivar","Vietnam":"Vietnamese Dong","Western Sahara":"Moroccan Dirham",
    "Yemen":"Yemeni Rial","Zambia":"Zambian Kwacha","Zimbabwe":"Zimbabwe Dollar"}
    
repeat1 = True
while(repeat1):
    repeat2 = True
    country = input("¿De qué país quieres saber su moneda?: ")
    if (list(currencies.keys()).count(country)):
        print("La moneda de " + country + " es " + currencies[country])
    else: 
        print(country + " no es un país o no está en el diccionario.")
    while(repeat2):
        answer = input("¿Quieres hacer otra consulta (S/N)?: ")
        if(answer == "S"):
            repeat2 = False
        elif(answer == "N"):
            repeat1 = False
            repeat2 = False
            print("Programa finalizado.")
        else:
            print("Respuesta no conocida. Indique si quiere hacer otra consulta (S/N)")