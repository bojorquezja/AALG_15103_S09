def multiplicacion(u, v):
    tamaño_u = len(str(u))
    tamaño_v = len(str(v))
    n = max(tamaño_u, tamaño_v)

    if n == 1:
        return u * v
    else:
        s = n // 2
        divisor = 10 ** s
        w_izquierda = u // divisor
        x_derecha = u % divisor
        y_izquierda = v // divisor
        z_derecha = v % divisor

        multiplicar_wy = multiplicacion(w_izquierda, y_izquierda)
        multiplicar_wz = multiplicacion(w_izquierda, z_derecha)
        multiplicar_xy = multiplicacion(x_derecha, y_izquierda)
        multiplicar_xz = multiplicacion(x_derecha, z_derecha)

        producto = (multiplicar_wy * (10 ** (2 * s))) + ((multiplicar_wz + multiplicar_xy) * divisor) + multiplicar_xz

        return producto



numero1 = 1234

numero2 = 5678

respuesta = multiplicacion(numero1, numero2)

print(f"la respuesta es: {respuesta}")