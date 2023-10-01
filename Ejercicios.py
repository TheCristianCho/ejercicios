#Participantes: Vicente Velez Taylor, Cristian Alonso Giraldo Caceres, Luis Felipe Rojas Cacierra, Anderson Andres arbol 


'''
1 Escribir un programa que muestre por pantalla la cadena ¡Bienvenido a la clase de Algoritmia y Programacion.
'''
print('bienvenido a clase de algoritmia y programacion')

'''
2 Escribir un programa que alamacene la cadena ¡Bienvenido a la clase de Algoritmia y Programacion! en una variable y 
luego muestre por pantalla el contenido de la variable
'''

Cadena = ('Bienvenido a la clase de algoritmia y programacion')
print(Cadena)


'''
3 Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca
muestre por pantalla la cadena ¡Hola,<nombre>¡Bienvenido a la clase de Algoritmia y Programacion ,donde<nombre>es 
el nombre que el usuario haya introducido
'''

nombre = input('por favor introducir el nombre: ')
print('¡Hola '+nombre+"," ' Bienvenido a la clase de algoritmia y programacion!' )

"""
4 Esbrir un programa que pregunte al usuario por el numero de horas trabajadas y el coste por hora.
Despues debe mostrar por pantalla la paga que le corresponde.
"""

numerosdehorastrabajadas = int(input('por favor digite el numero de horas trabajadas: '))
costedehoras = int(input('por favor digite el pago de horas: '))
pagodehoras = numerosdehorastrabajadas * costedehoras
print('el pago correspondiente es de: ', pagodehoras)

'''
Ejercicio 5
Escribir un programa que lea un entero positivo introducido por el usuario y después muestre en 
pantalla la suma de todos los enteros desde 1 hasta La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
'''
n =int(input("Introduzca un número entero: "))
suma = n * (n+1)/2
print("La suma de los primeros enteros desde 1 hasta" " " +str(n)+ " es " + str(suma))

'''
6 Escribir un programa que pida al usuario su peso(en Kg)y estatura(en metros),
calcule el indicede masa corporal y lo almacene en una variable,y muestre por pantalla la frase Tu indice de masa corporal
es <imc>donde <imc>es el indice de masa corporal calculado redondeado con dos decimales.
'''

peso = float(input('por favor digitar su peso en kg: '))
altura = float(input('por favor digitar su altura: '))
imc = round(peso / (altura * altura),2)
print('su imc es de: ', imc)

'''
Ejercicio 7
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto 
<r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
'''
n = input('introduce el dividendo (entero): ')
m = input('introdusca el divisor (entero): ')
print(n + ' entre ' + m + ' da un cociente ' + str(int(n) // int(m)) + ' y un resto ' + str(int(n) % int(m)))

"""
8 Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""

cantidadainvertir = int(input('que cantidad desea invertir: '))
interesanual = float(input('por favor escribir el interes anual: '))
numerodeañosainvertir = int(input('digite la cantidad de años que se va a invertir: '))
cantidaddeobtencion = (round(cantidadainvertir * (interesanual / 100 + 1) ** numerodeañosainvertir, 2))
print('el capital obtenido seria de: ', cantidaddeobtencion)

'''
Ejercicio 9
Una juguetería tiene mucho éxito en dos de sus productos: Carros, Aviones y Balones. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
así que deben calcular el peso de los Carros, Aviones y Balones que saldrán en cada paquete a demanda. Cada Carro pesa 7 kg, cada avión pesa 12.5 kg y cada Balón pesa 5.3kg. 
Escribir un programa que lea el número de Carros, Aviones y Balones vendidos en el último pedido y calcule el peso total del paquete que será enviado.
'''
PesoCarros = 7
PesoAvión = 12.5
PesoBalón = 5.3
Carro = int(input("Ingresar la cantidad de Carros: "))
Avión = int(input("Ingresar la cantidad de Aviones: "))
Balón = int(input("Ingresar la cantidad de Balones: "))
Peso_Total = PesoCarros * Carro + PesoAvión * Avión + PesoBalón * Balón
print("El peso total del paquete es: ", Peso_Total)

'''
Ejercicio 10
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 11% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo, tercer, cuarto y quinto años. Redondear cada cantidad a dos decimales.
'''
Inversion = float(input("Introduce la inversión inicial: "))
Interes = 0.11
Balance1 = Inversion * (1 + Interes)
print("Balance tras el primer año: " + str(round(Balance1, 2)))

Balance2 = Balance1 * (1 + Interes)
print("Balance tras el segundo año: " + str(round(Balance2, 2)))

Balance3 = Balance2 * (1 + Interes)
print("Balance tras el tercer año: " + str(round(Balance3, 2)))

Balance4 = Balance3 * (1 + Interes)
print("Balance tras el cuarto año: " + str(round(Balance4, 2)))

Balance5 = Balance4 * (1 + Interes)
print("Balance tras el quinto año: " + str(round(Balance5, 2)))

'''
Ejercicio 11
Una panadería vende barras de pan a $ 5.000 cada una. El pan que no es del día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
'''
Barras_pan= int(input("Introducir el número de barras vendidas no frescas: "))
Precio = 5000
Pan_descuento = 0.6
coste_final= Barras_pan * Precio * (1 - Pan_descuento)
print("el coste de una barra de pan fresca es: " +str(Precio) + "$")
print("Descuento a barra de pan que no esta fresca es: " +str(Pan_descuento*100) + "%")
print("El coste final es: " + str(round(coste_final, 2)) + "$")

'''
Ejercicio 12
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces 
como el número introducido.
'''

nombre_del_usuario = input(" ¿Cuál es tú nombre? " )
n = input("Introduzca el número entero:")
print((nombre_del_usuario + "\n") * int(n))

"""
13 Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces,
una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""

name = input("¿Cómo te llamas? ")
print(name.lower())
print(name.upper())
print(name.title())

'''
14Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, 
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre
'''

nombre = input("¿Cómo te llamas?: ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")

'''
15 Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +57, y la extensión tiene dos dígitos 
(por ejemplo +57-3188446824-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el 
prefijo y la extensión.
'''

numero_de_telefono = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', numero_de_telefono[4:-3])

'''
16 Escribir un programa que pida al usuario que introduzca una frase en la consola y 
muestre por pantalla la frase invertida.
'''

frase = input("Introduce una frase: ")
print(frase[::-1])

'''
17 Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
y después muestre por pantalla la misma frase, pero con la vocal introducida en mayúscula.
'''

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(frase.replace(vocal, vocal.upper()))

'''
18 Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla 
otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio sigma7.com.co.
'''

correo_electronico = input("Introduce tu correo electrónico: ")
print(correo_electronico[:correo_electronico.find('@')] + '@sigma7.com.co')

'''
19 Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, 
el día, el mes y el año.
'''
 
fecha = input('introduce la fecha que nacimiento en formato DD/MM/AAAA: ')
print(type(fecha))
dia = fecha[fecha.find('/')+1:]
mes_año = fecha[fecha.find('/')+1:]
print(mes_año)
mes = mes_año [:mes_año.find('/')]
año = mes_año [mes_año.find('/')+1:]
print('dia', dia)
print('mes', mes)
print('año', año)

'''
Ejercicio 20
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
'''

cesta = input ("Introduzca los productos de la cesta de la compra por separados: ")
print(cesta.replace(",", "\n"))

'''
Ejercicio 21
Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
'''

producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades:6d} unidades x {precio:8.2f}$ = {total:14.2f}$'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))



