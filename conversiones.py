import sys

# Se guarda en variables los parametros parados por argv
# Primero se consulta por pesos Chilenos para poder ocuparlo posteriormente en las otras funciones.
pesosChilenos = float(sys.argv[4])
solPeruano = float(sys.argv[1]) * pesosChilenos
pesoArgentino = float(sys.argv[2])  * pesosChilenos
dolarAmericano = float(sys.argv[3])  * pesosChilenos

#Se imprime
print(f'''
Los {pesosChilenos} pesos equivalen a:
{solPeruano} Soles
{pesoArgentino} Pesos Argentinos
{dolarAmericano} Dólares
''')