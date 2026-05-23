def calcular(n1, n2):
    cifra = max(len(str(abs(n1))), len(str(abs(n2))))
    if cifra <= 1:
        return n1 * n2
    
    mitad = cifra// 2
    izquierda = n1 // (10 ** mitad) 
    derecha = n1 % (10 ** mitad) 
    nuevoizquierda = n2 // (10 ** mitad) 
    nuevoderecha = n2 % (10 ** mitad)
    
    return (calcular(izquierda, nuevoizquierda) * (10 ** (2 * mitad)) +
    (calcular(derecha, nuevoizquierda) + calcular(izquierda, nuevoderecha)) * (10 ** mitad) +
    calcular(derecha, nuevoderecha))

n1 = 1234

n2 = 5678

resultado = calcular(n1, n2)

print(f"{n1} x {n2} = {resultado}")

print(f"Verificación: {n1 * n2}")