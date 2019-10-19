"""
Autor: Moises Preciado
Objetivo: Primer programa en python
Nombre: Funcion.py
"""
#---------------------------------------------------------------
# Funcio para invocar mensaje
#---------------------------------------------------------------

def printMensaje():
    print("Funcion que no retorna nada")

#---------------------------------------------------------------
# Funcio para imprimir un argument
#---------------------------------------------------------------
def printArgumento(cad):
    print("recibi: ", cad)

#---------------------------------------------------------------
# Funcio para regresar un valor
#---------------------------------------------------------------
def regresaSuma(n1,n2):
    return n1+n2

#---------------------------------------------------------------
# Funcio para mostrar la etrucura if
#---------------------------------------------------------------
def comparaEnteros(n1,n2):
    if n1>n2:
        print("El mayor valor es n1 ",n1)
    elif n2>1:
        print("El mayor valor es n2 ",n2)
    else:
        print("Los numeros son iguales: ",n1, ",", n2)

#---------------------------------------------------------------
# Funcio para mostrar estructura repetitiva while
#---------------------------------------------------------------
def contarEnteros(n1):
    if (n1>0):
        i=0
        while i<=n1:
            print(i)
            i+=1
    else:
        print("Porfavor Teclea un mumero mayor que 0")

#---------------------------------------------------------------
# Funcio para mostrar estructura repetitiva for
#---------------------------------------------------------------
def contarFor(n1):
    if n1>0:
        for i in range(n1):
            print(i)
    elif n1<0:
        for i in range(n1,0):
            print(i)


def main():
    ciclo = 'S'
    while ciclo == 'S':
        n1 = int(input("Introduce numero uno: "))
        n2 = int(input("Introduce numero dos: "))

        #invocamos funcion printMensaje
        printMensaje()
        #Invocamos funcion printMensaje
        printArgumento("Hola")
        #Invocamos la funcion regresaSuma
        print("La suma es= ",regresaSuma(n1,n2))
        #Invocamos la funcion comparaEnteros
        comparaEnteros(n1,n2)
        #Invocamos funcion contarEnteros
        contarEnteros(n1)
        #Invocamos funcion contarFor
        contarFor(n1)

if __name__ == "__main__":
    main()