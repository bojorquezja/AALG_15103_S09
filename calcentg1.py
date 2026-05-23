def mult(u, v):
    if u < 10 or v < 10:
        return u * v
    else:
        n = max(len(str(u)), len(str(v)))
        s = n // 2
        potencia = 10 ** s

        w = u // potencia
        x = u % potencia
        y = v // potencia
        z = v % potencia

        return (mult(w, y) * (10 ** (2 * s)) + (mult(w, z) + mult(x, y)) * potencia + mult(x, z))


u = int(input("Ingrese el primer número: "))
v = int(input("Ingrese el segundo número: "))

resultado = mult(u, v)


print("Resultado:", resultado)