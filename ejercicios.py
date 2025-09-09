
#1
#Escribir un programa en Java que imprima por pantalla la frase “Hola, ya se imprimir frases”.
print ("Hola, ya se imprimir frases")

#2
#Escriba un programa que lea temperaturas expresadas en grados Fahrenheit y las convierta a grados Celsius mostrándola. 
#El programa finalizará cuando lea un valor de temperatura igual a 999. La conversión de grados Farenheit (F) a Celsius (C) está dada por C = 5/9(F − 32).
F = float(input("Dé una temperatura en grados Fahrenheit (F) para pasarla a grados Celsius (C)  "))
C = float

if ((F != 999)):
    C = 5/9*(F - 32)
    print(C) 
    F = float(input("Dé una temperatura en forma numerica en grados Fahrenheit (F) para pasarla a grados Celsius (C)  "))

#3
#Escribir un programa en Java que convierta de euros a dólares. 
# Recibirá un númerodecimal correspondiente a la cantidad en euros y contestará con la cantidad correspondiente en dolares.
Euro = float(input("Dé una cantidad numerica de euros para pasara a dolares  "))
Dolar = float

if ((Euro > 0)):
    Dolar = Euro * 1.17 
    print(Dolar) 
    Euro = float(input("Dé una cantidad numerica de euros para pasara a dolares  "))

#4
boleano= str(5+3)
print=(type(boleano), boleano)
