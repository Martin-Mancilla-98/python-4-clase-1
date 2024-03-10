from enum import Enum

class Vertebra(Enum):
    VER='vertebrado'
    INV='Invertebrado'

class CantPata(Enum):
    UNA =1
    DOS =2
    TRES =3
    CUAT = 4

class Raza (Enum):
    GOLD='Gold Retriever'
    CANI='caniche'
    PITB='Pitbull'
    BEAG='Beagle'



class Animal():
    def __init__(self,cantidaddePatas,tipo):
        self.cantidaddePatas=cantidaddePatas
        self.tipo=tipo
    
    def comer(self):
        print('Estoy comenzando a comer')

class Perro(Animal):
    def __init__(self,nombre,raza,cantidaddePatas,tipo):
        self.nombre=nombre
        self.raza=raza

        super().__init__(cantidaddePatas,tipo)
        self.nombre=nombre
        self.raza=raza

    def correr(self):
        print('esta corriendo ')

class aguila (Animal):
    def __init__(self,cantidaddePatas,tipo):
        self.cantidaddePatas=cantidaddePatas=cantidaddePatas
        self.tipo=tipo
    
        super().__init__(cantidaddePatas,tipo)
    
    def volar(self):
        print('estoy volador')

miPerro=Perro(CantPata.CUAT.value,Vertebra.VER.value,'Roco',Raza.BEAG.value)
miPerro.correr()
miPerro.comer()

pajaro=aguila(CantPata.DOS.value,Vertebra.INV.value)

pajaro.volar()
pajaro.comer()