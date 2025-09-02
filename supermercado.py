# en el supermercado se le dara un descuento del 5% por compras superiores a 50000 el 8% si las compras son mayores a 80000 y 10% si fueron mas de 100000
print("si el valor de la compra fue superios a 50000 se le aplicara un descuento del 5%")
print("si el valor de la compra fue superios a 80000 se le aplicara un descuento del 8%")
print("si el valor de la compra fue superios a 100000 se le aplicara un descuento del 10%")
valormercado=int(input("digite el valor de las compras:"))


if(valormercado>=50000 and valormercado<80000):
    descuento=(valormercado*5/100)
    valormercado=valormercado-descuento
    print(f"despues del descuento del 5% realizado el valor del mercado equivale a {valormercado}")
elif (valormercado>=80000 and valormercado<100000):
    descuento=(valormercado*8/100)
    valormercado=valormercado-descuento
    print(f"despues del descuento del 8% realizado el valor del mercado equivale a {valormercado}")
elif (valormercado>=100000):
    descuento=(valormercado*10/100)
    valormercado=valormercado-descuento
    print(f"despues del descuento del 10% realizado el valor del mercado equivale a {valormercado}")
else:
    print(f"el valor de compras  {valormercado} fue menor a 50000 por consecuente es imposible realizar un descuento")
