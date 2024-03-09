import sys

# Inicializo variables globales
texto = []
distinctWords = {}
distinctCharacters = []

# Leo el archivo lorem_ipsum.txt y guardo el contenido en la variable initialFile
with open(f"{sys.argv[1]}", "r") as file:
    initialFile = file.read()

# Separo el texto por los espacios en blanco, y los almaceno en una lista.
# Posteriormente convertirla en un set, el cual automaticamente quita los duplicados.
texto = initialFile.split(" ")
distinctWords = set(texto)

# Recorro el string original, para que revise cada caracter presente en este
# Si no esta presente en la lista que almacena caracteres, se añade.
for character in initialFile:
    if(not character in distinctCharacters):
        distinctCharacters.append(character)

# Imprime el resultado
print(f'''
El numero de caracteres distintos es: {len(distinctCharacters)}
El numero de palabras distintas es: {len(distinctWords)}
''')