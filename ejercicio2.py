n = int(input("Introduce un número: "))
def fact(n):
    if n < 1:
        return 1
    return n * fact(n-2)
try:
    if n <= 0:
        raise ValueError
    p = fact(n)
    print(p)
except ValueError:
    print("Es un número negativo")