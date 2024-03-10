"""
def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

i=1
while i==1:
    num1=float(input("ingrese el valor"))
    num2=float(input("ingrese el valor 2"))
    
    eleccion=input("ingrese la accion a \n\tA->suma \n\t B->resta \n\t Respuesta")

    if eleccion=='A' or eleccion=='a':
        print(f'el resultado de {num1}+{num2}={suma(num1,num2)}')
    
    elif eleccion=='B' or eleccion=='b':
        print(f'El resultado de {num1}-{num2}={suma(num1,num2)}')
    else:
        print("ingreso una opcion incorrecta")
    
    respuestaUsuario=input("Desea seguir operando:\n\t ingrese 0 ->no\n\tIngrese 1 ->Si \n\t Resouesta ")
    i=int(respuestaUsuario)

    """


def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def main():

    if__name__=="__main__":
    main()

    numero1=int(input('Ingrese el numero entero'))
    numero2=int(input('Ingrese el numero entero'))

    salir=False

    while not salir:
        print("A para sumarlos ")
        print("B para restarlos ")
        print("x para salir")

        opcion=input("ingrese a o b").upper()

        match opcion:
            case 'A':
                suma(numero1,numero2)
            case 'B':
                resta(numero1,numero2)
            case 'X':
                salir=True
            case _:
                print("opcion invalida reintente ")

def accion_A(a,b):
    return a+b

def accion_b(a,b):
    return a+b

def main():
    while True:
        opcion=input("ingrese 1 para sumar o 2 para miltiplicar")

        if opcion in('1','2'):
            opcion=int (opcion)

            num1=float(input("ingrese el primer numero"))
            num2=float(input("ingrese el segundo numero"))

            if opcion==1:
                resultado=accion_A(num1,num2)
                print("El resultado de la accion A es ",resultado)
            else:
                resultado=accion_b(num1,num2)
                print("El resultado de la accion Bes ",resultado)