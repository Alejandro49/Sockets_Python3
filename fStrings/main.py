import datetime

nombre = "Alejandro"
apellido = "Llorente"

# formateando String de forma tradicional con .format
# frase = "Mi nombre es {} {}".format(nombre, apellido)

# Usando fString; Mucho más intituitivo
# frase = f"Mi nombre es {nombre} {apellido}"

# Incluso se pueden aplicar metodos a las variables de dentro
frase = f"Mi nombre es {nombre.encode('utf-8')} {apellido.upper()}"

print(frase)

# Bucle con variable interna
'''for n in range(1,11):
    frase = f"El valor es {n}"
    print(frase)'''

# fString permite añadir ceros adelante de un número

for n in range(1,11):
    #Primer digito que va a preceder : 0
    #Número de digitos totales que va a tener el número: 5
    frase = f"El valor es {n:05}"
    print(frase)

# Jugando con números decimales
pi = 3.14159265
frase = f"Pi es igual a {pi:.4f}"
print(frase)

# Fechas
hoy = datetime.datetime.now()

hora = time.time()

frase = f"Estamos a {hoy}"
print(frase)

frase = f"Estamos a {hoy:%B %d, %Y}"
print(frase)

