'''
Entrada y salida de datos
'''

'''
la formula que utilizaremos es la siguiente

(c+5)(b²-3ac)a²            OJO: recuerden que los espacios basias despues de los ()estos espacios() cuentan
_________________                como multiplicacion, asi seia entonces: (c+5)*(b²-3ac)*a²/4
        4a                    recuerden que para elevar al cuadrado un numero o potecia es con **

'''

a = float(input("Ingrese el valor de (a): "))
b = float(input("Ingrese el valor de (b): "))
c = float(input("Ingrese el valor de (c): "))

r= ((c+5)*(b**2-3*a*c)*a**2)/(4*a)

print(f"Su resultado es : {r}")
