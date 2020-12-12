import requests #if not installed in Windows: pip install requests

# función que imprime por pantalla cada uno de los comentarios
def printComment(comment):
    print('\tcomment[id] =', comment['id'])
    print('\tcomment[body] =', comment['body'])
    print('\tcomment[name] =', comment['name'])
    print('\tcomment[email] =', comment['email'])
    print('\tcomment[postId] =', comment['postId'])

# función que imprime por pantalla todos los comentarios
def printComments(comments):
    for i in range(len(comments)):
        print('i =', i)
        printComment(comments[i])

url='https://jsonplaceholder.typicode.com/posts/1/comments'

# hacemos un petición GET a la URL
response = requests.get(url)

# convierte la respuesta a un diccionario Python
jsonList = response.json()
printComments(jsonList)
