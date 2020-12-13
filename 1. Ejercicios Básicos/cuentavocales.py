vowels = ["a","e","i","o","u"]
found = []
frase = input("Introduzca una frase para contar sus vocales: ")
for vowel in vowels:
    print("Hay " + str(frase.count(vowel))+ " " + vowel + " en tu frase.")