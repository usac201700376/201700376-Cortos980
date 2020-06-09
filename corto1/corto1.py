import os
fille = open("collatz.txt", "a")
def secuencia(n):
    numeros=[n]
    for i in range(1,n):
        a=n
        while(n>2):
            if(a%2==0):
                a//=2
                numeros.append(a)
                n=a
            else:
                a=3*a+1
                numeros.append(a)
                n=a
            a=n
    return numeros
def sec(n):
    for i in range(n+1):
        finales=secuencia(i)
        print(finales)
    return finales
a=int(input("ingrese un numero: "))
sec(a)
