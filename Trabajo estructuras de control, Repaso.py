# Trabajo estructuras de control, Repaso de programacion 

#1 Imprimir la frase hola ya se imprimir frases

print("Hola!, ya se como imprimir frases")

#2 Programa que imprima un numero

print("Esto es un numero:", 3)

#3 Programa que imprima un numero decimal

print("Esto es un numero decimal:", 2.4)

#4,5,6,7 Crear un programa el cual sume, reste, multiplique y divide los numeros 1234 y 532

def operaciones(x, y):
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    division = x / y
    operacion = 0
    while operacion == 0:
        operacion_a_realizar = input("Selecciona la operacion a realizar entre los numeros 1234 y 532 \nSuma (s), Resta (r), Multiplicacion (m), Division(d) \n")
        if operacion_a_realizar == "s":
            print(suma)
            operacion = 1
        elif operacion_a_realizar == "r":
            print(resta)
            operacion = 1
        elif operacion_a_realizar == "m":
            print(multiplicacion)
            operacion = 1
        elif operacion_a_realizar == "d":
            print(division)
            operacion = 1 
        else:
            print("Ingrese una operacion valida")
    
print(operaciones(1234, 532))

#8 Imprimir los numeros de 1 a 3

numeros = []
for i in range (1, 4):
    numeros.append(i)

print (numeros)

#9 Imprimir los numeros de 1 al 9

numeros = []
for i in range (1, 10):
    numeros.append(i)
    
print(numeros)

#10 Imprimir los numeros del 1 al 10000

numeros = []
for i in range(1, 10001):
    numeros.append(i)
    
print(numeros)

#11 Imprimir los numeros del 5 al 10

numeros = []
for i in range(5, 11):
    numeros.append(i)
    
print(numeros)

#12 Imprimir los numeros del 5 al 15

numeros = []
for i in range(5, 16):
    numeros.append(i)
    
print(numeros)

#13 Imprimir los numeros del 5 al 15000

numeros = []
for i in range(5, 15001):
    numeros.append(i)
    
print(numeros)

#14 Imprimir la palabra "hola" 200 veces

for i in range (1, 201):
    print("Hola")
    
#15 Imprimir cuadrado de los primeros 30 numeros naturales

numeros_naturales = []
for i in range(1, 31):
    y = i * i
    numeros_naturales.append(y)

print(numeros_naturales)

#16 Imprima la multiplicacion de todos los primeros 20 numeros naturales

multi = 1
for i in range(1, 21):
    multi *= i
    
print(multi)

#17 Imprimir el resultado de sumar los primeros 100 cuadrados

cantidad_sumada = 0
for i in range(1, 101):
    cuadrados = i * i
    cantidad_sumada += cuadrados
    
print(cantidad_sumada)

#18 Lea un numero y sume los siguientes 100 digitos

def suma_digitos(x):
    for i in range(x + 1 , x + 101):
        x += i
    return x

a_sumar= int(input("Cual es el numero al que desea sumar sus siguientes cien numeros?: "))

print(suma_digitos(a_sumar))

#19 Convertir de euros a dolares

def conversion(euro):
    conversiones = euro * 1.17
    return conversiones

euros = float(input("Ingrese cantidad de euros a convertir a dolares: "))

print(conversion(euros))

#20 Calcular el area de un rectangulo 

def area_rectangulo(altura, ancho):
    area = altura * ancho
    print("El area del rectangulo es:")
    return area

rec_altura = float(input("Altura del rectangulo: "))
rec_ancho = float(input("Anchura del rectangulo: "))

print(area_rectangulo(rec_altura, rec_ancho))

#21 Lea dos numeros y detecte el menor

def numero_mayor_menor(a, b):
    if a > b:
        print(str(a) + " es el numero mayor y " + str(b) + " es el numero menor")
    elif b > a:
        print(str(b) + " es el numero mayor y " + str(a) + " es el numero menor")   

num1 = float(input("Ingrese el numero 1: "))
num2 = float(input("Ingrese el numero 2: ")) 

print(numero_mayor_menor(num1, num2))