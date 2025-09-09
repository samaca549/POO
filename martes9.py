class Perro:
    #constructor
    #se esta construyendo una clase 
    #el constructor construye un ejemplo esto significa darles valores a los atributos
    #es igual que una funcion con un parametro especial__init__ no es modificable
    #self (uno mismo) al objeto que usted esta creando se le asignara las siguientes variables y todos los atributos
    #le voy asignar los atributos
    def __init__(self, edad, nombre, color):
        self.edad=edad
        self.nombre=nombre
        self.color=color

    #metodos
    def ladrar(Self):
        print("Guau Guau")
    
    def saludar(self):
        print(f"hola el nombre del perro es {self.nombre}")

    def concentir(self):
        print(f"el usuario esta concintiendo al perro {self.nombre}")
    
    def alimentar(self):
        print(f"el usuario esta alimentando al perro")
    #hacer feliz al perro
    def hacerfeliz(self):
        print(f"el perro {self.nombre} esta feliz porque ya lo alimentaron y lo concintieron")

mi_perro=Perro(5, "tobi", "azul")
print(mi_perro.edad)
mi_perro.ladrar()
mi_perro.saludar()
def preguntar(x):
    print("desea concentir al perro ")
    x=str(input("digite si o no:"))
    if(x=="si"):
        mi_perro.concentir()
    elif(x=="no"):
        print("pienselo")
        while (x!="si"):
            print("desea concentir al perro: ")
            x=str(input("digite si o no:"))
        if(x=="si"):
            mi_perro.concentir()
print("desea alimentar al perro ")
decision1=str(input("digite si o no:"))
if(decision1=="si"):
    mi_perro.alimentar()
elif(decision1=="no"):
    print("pienselo")
    while (decision1!="si"):
        print("desea alimentar al perro: ")
        decision1=str(input("digite si o no:"))
    if(decision1=="si"):
        mi_perro.alimentar()
preguntar()
mi_perro.hacerfeliz()
#cuando requiero un int es para realizar operaciones

