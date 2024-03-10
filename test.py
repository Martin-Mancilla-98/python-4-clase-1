suma=10+5
print("el numero es")
print(suma)
nombres=["tito","Juan","Pepe","Martin","Luis"]
# por cada elemento "nombre" en la lista nombres

for nombre in nombres:
    print(nombre);

persona1={
    "nombre":"pepe",
    "apellido":"Gomez",
    "edad":30,
    "altura":1.75
}
for e in persona1:
    print(e)

for e in persona1.values():
    print(e)

for e in persona1.keys():
    print(e)
print("----------------")
for e in persona1.items():
    print(e)
print("----------------")

for dato in persona1.items():
    for e in dato:
        print(e)

for p in persona1:
    print(f'{p}: {persona1[p]}')

def sumar_iva(nombre,precio,porIva):
    resultado=precio*porIva
    saludo=f'Hola {nombre} precio total {resultado}'
    return saludo


print(sumar_iva("pablo",400,1.21))
"""
i=1
while i==1:
    numero1=int(input("ingrese el primer numero"))
    numero2=int(input("ingrese el segundo numero"))
    
    x=input("ingrese la opcion 1 o2 ")

if x==1:
    print(suma(numero1,numero2))
if x==2:
    print(resta(numero1,numero2))


def accion1(numero1,numero2):
    return(numero1+numero2)
def accion2(numero1,numero2):
    return(numero1-numero2)
"""
#forma 2 

i=1
while i==1:
    numero1=float(input("ingrese el primer numero:"))
    numero2=float(input("ingrese el segundo numero"))

    eleccion=input("ingrese la accion \n\tA-> suma\n\tB--> resta\n\trespuesta:")
    
    if eleccion=='A' or eleccion=='a':
        print(f'el resultado{numero1}+{numero2}={suma(numero1,numero2)}')
    elif eleccion=='B' or eleccion=='b':
        print(f'el resultado{numero1}-{numero2}={suma(numero1,numero2)}')
    else:
        print("ingreso una opcion incorrecta")
    
    respuestaUsuario=input("desea segui operando: \n\t ingrese 0->No\n\t ingrese 1 ->SI\n\tRespuesta:")
    i=int(respuestaUsuario)