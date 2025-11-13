class NuevaExcepcion(Exception):
    pass
    print("Error en valores")

try:
    a = 4
    b = 0
    c = a%b
    if c == 0:
        raise ValueError
    
except NuevaExcepcion:
    print("El número es par")
except ValueError:
    print("No se puede tener ese valor")
except ZeroDivisionError:
    print("División por cero")
