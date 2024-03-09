recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

# !!! SEGUN EL ENUNCIADO ES 02 DE FEBRERO, DISTINTO AL RESULTADO MOSTRADO EN PDF, ME GUIO POR ENUNCIADO
# Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”.
recordatorios.append(['2021-02-02', '06:00', 'Empezar el año'])

# Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado. Editar
# de tal manera que sea el 16 de Julio.
for index, record in enumerate(recordatorios):
    if record[0] == '2021-07-15':
        recordatorios[index][0] = '2021-07-16'

# Lamentablemente le tocará trabajar el día del trabajo. Elimine el evento del día del trabajo. 
for index, record in enumerate(recordatorios):
    if record[0] == '2021-05-01':
        recordatorios.pop(index)

# Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

# Los eventos deben siempre editarse de tal manera que mantengan su
# orden en el tiempo.
recordatorios.sort()

# Output
print(recordatorios)
