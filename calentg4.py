def multiplicacionenteros(x, y):
    if x < 10 or y < 10:
        return x * y
    
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    a, b = divmod(x, 10**m)
    c, d = divmod(y, 10**m)

    z2 = multiplicacionenteros(a, c)
    z0 = multiplicacionenteros(b, d)
    z1 = multiplicacionenteros(a, d) + multiplicacionenteros(b, c)

    return (z2 * 10**(2*m)) + (z1 * 10**m) + z0

try:
    num1 = int(input("Ingresa el primer número largo: "))
    num2 = int(input("Ingresa el segundo número largo: "))
    resultado_mult = multiplicacionenteros(num1, num2)
    resultado_real = num1 * num2
    print("--------------------");
    print(f"Resultado de multiplicación es: {resultado_mult}")

    print(f"Resultado de la operación tradicional: {resultado_real}")

    print("--------------------");

    if resultado_mult == resultado_real:

        print("\n Los resultados son iguales")

    else:

        print("\nError: Los resultados no coinciden.")

except ValueError:

  print("Por favor, ingresa solo números enteros.")