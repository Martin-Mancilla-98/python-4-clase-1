"""
class Auto:
    def acelera(self):
        print("Me trasporto en 4 ruedas")

class Moto:
    def acelera(self):
        print("Me trasporto en 2 ruedas")
    
class Camion:
    def acelera(self):
        print("Me trasporto en 18 ruedas")

mivehiculo=Auto()

def vehiculoacelera(vehiculo):
    vehiculo.acelera()

vehiculoacelera(mivehiculo)


class Algo:
    def __init__(self,nombre,apellido):
        self.__nombre= nombre
        self.apellido=apellido

algo=Algo("Juan","Perez")

print(algo.__nombre)
print(algo.apellido)
"""

class Productos:
    def __init__(self,id,titulo,autor,precio,stock):
        self.id=id
        self.titulo=titulo
        self.autor=autor
        self.precio=precio
        self.stock=stock

    def mostrarProductos(self):
        pass


class Libro(Productos):
    def __init__(
            self,
            id,
            titulo,
            autor,
            precio,
            stock,
            editorial, #propio de Libro 
            generoLiterario #propio de Libro -enu
        ):

        super().__init__(id,titulo,autor,precio,stock)
        self.editorial=editorial
        self.generoLiterario=generoLiterario
    
    def mostrarProductos(self):
        print(f'id:{self.id}')
        print(f'Titulo:{self.titulo}')
        print(f'autor:{self.autor}')  
        print(f'precio:{self.precio}')    
        print(f'stock:{self.stock}')  
        print(f'editorial:{self.editorial}') 
        print(f'generoLiterario:{self.generoLiterario}')     
    

class Pelicula(Productos):
    def __init__(
            self,
            id,
            titulo,
            autor,
            precio,
            stock,
            clasificacion, #propio de Pelicula 
            generoCine #propio de Pelicula -enu
        ):

        super().__init__(id,titulo,autor,precio,stock)
        self.clasificacion=clasificacion
        self.generoCine=generoCine 

    def mostrarProductos(self):
        print(f'id:{self.id}')
        print(f'Titulo:{self.titulo}')
        print(f'autor:{self.autor}')  
        print(f'precio:{self.precio}')    
        print(f'stock:{self.stock}')  
        print(f'clasificacion:{self.clasificacion}') 
        print(f'generoCine:{self.generoCine}')     
    
class Musica(Producto): 
    def __init__(
            self,
            id,
            titulo,
            autor,
            precio,
            stock,
            formato, # CD / VINILO / Cassette
            generoMusica # Rock / Pop / Clasica / Trap
        ):
        super().__init__(id, titulo, autor, precio, stock)
        self.formato = formato
        self.generoMusica = generoMusica
    def mostrarProducto(self):
        print(f'id: {self.id}')
        print(f'titulo: {self.titulo}')
        print(f'autor: {self.autor}')
        print(f'precio: {self.precio}')
        print(f'stock: {self.stock}')
        print(f'formato: {self.formato}')
        print(f'generoMusica: {self.generoMusica}')
"""
miLibro=Libros(id,titulo,autor,precio,stock,editorial,generoLiterario )
"""

miLibro=Libro("1","1984","Geoge orwell",12000,19,"anagrama","novela" )
miLibro.mostrarProductos()

miPeli= Pelicula("2","Cars","pixar",5000,23,"ATP","Infantil")

miPeli.mostrarProductos()