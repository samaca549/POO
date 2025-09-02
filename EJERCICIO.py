## El marcado for refleja
for x in range (5):
    print(f"hola {x}")

## this is a
##todos tienen un bloque anidado en el que se puede trabajar los dos puntos, la sangria son importantes la ausencia de este significa escribir de manera incorrecta la sintaxis del bloque
##los dos puntos exigen que existan dos lineas de codigo, reglas semanticas 
##dentro del range puede haber multiples parametros si solo se pono range(5) ira de o a 4

for x in range (5, 9, 3):
    print(f"la intencion del tercer numero tiene la intencion de dar saltos de a 3: {x}")

#para dar pasos negativos se colocan de manera contraria es decir ya no se pone el menor y despues el mayor si no al contrario (10, 2, -1) y en el tercer numero me indica de cuanto son los pasos
for x in range (10, 2, -1):
    print(f"la intancion es ir de orden contrario {x}")

xp=0
xf=21
for x in range (xp, xf, 2):
   if(x%4==0):
       print(f"los multiplos de 4 entre en xp y xf son {x}")
    
       
# == ese simbolo representa una operacion de comparacion y el = es de asignacion
# para que aparesca el 20 en el codigo de arriba fue necesario asignar el valor de xp 21 porque el for va hasta n-1 es decir 20
# lo interesante del elif es que debe tener un if primero para funcionar
# en el supermercado se le dara un descuento del 5% por compras superiores a 50000 el 8% si las compras son mayores a 80000 y 10% si fueron mas de 100000
# para poder tener  dos condiciones en un if se utiliza and

#funcion 
#return sirva para recolectar datos
def obtenermultiplos(n):
    for x in range (xp, xf, ):
        if(x%4==0):
            print(f"los multiplos de {n} entre en xp y xf son {x}")    
def main():
    obtenermultiplos(5)
if(__name__=="_main_"):
    main()

#if(_name_) organizacion con lo que se va ejecutar, le va a dar prioridad a la ejecucion, va ejecutar un funcion llamada _main_
#declarar valores bool si 
boleano=True
print(type(boleano), boleano)
#principales tipos de datos: boleano, entero, decimal y string
#el objeto bool puede comportarse como un objeto 
boleano= 1
print(type(boleano), boleano)
#el ejemplo de arriba es entero
boleano="1"
print(type(boleano), boleano)
boleano=("1"==1)
print(type(boleano), boleano)
# el ejemplo de arriba es boleano, la operacion de comparacion devuelve siempre verdadero o falso.
boleano="char"+"char"
print(type(boleano), boleano)
# las operacion de arriba esta contatenando el resultado en la consola es charchar
# los unicos simbolos que se pueden utilizar para contatenar + y *
#para multiplicar se realiza char*3
# el bit es la unidad basica de informacion byte son 8 bits
boleano= str(5+3)
print=(type(boleano), boleano)