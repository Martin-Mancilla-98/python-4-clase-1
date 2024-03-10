from enum import Enum


class Vertebra(Enum):
    Ver='vertebrado'
    INV='Invertebrado'

class cantPata(Enum):
    UNA=1
    DOS=2
    TRES=3
    CUAT=4  

class Raza(Enum):
    Gold='Golden Retriever'
    CANI='Caniche'
    PITB='Pitbull'
    BEAG='Beagle'

class Animal():
    def __init__(
            self,
            cantidadpatas,
            tipo
        ):
        self.cantidadpatas=cantidadpatas
        self.tipo=tipo
        
    def comer(self):
        print("Estoy comiendo nom nom")

class Perro(Animal):
    def __init__(self,
        cantidadpatas,
        tipo,
        nombre,
        raza
        ):
        super().__init__(cantidadpatas,tipo)
        self.nombre=nombre
        self.raza=raza

        def correr(self):
         """   print("soy %s,un %s tengo %i"(self.nombre,self.raza,self.cantidadpatas))"""

class aguila(Animal):
    def __init__(self,cantidadpatas,tipo):
        self.cantidadpatas=cantidadpatas
        self.tipo=tipo
    
        super().__init__(
            cantidadpatas,
            tipo
        )
    

    def volar(self):
            """    print("soy %s,un %s tengo %i"(self.nombre,self.raza,self.cantidadpatas))"""

miPerro=Perro(cantPata.CUAT.value,Vertebra.ver.value,"Rocco",Raza.BEAG.value)
miPerro.correr()
miPerro.comer()

pajaro=aguila(cantPata.UNA.value,Vertebra,INV.value)