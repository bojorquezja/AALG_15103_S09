def merge(izq, der): 
    resultado = [] 
    while izq and der: 
        if izq[0] < der[0]: 
            resultado.append(izq[0]) 
            izq.pop(0) 
        else: 
            resultado.append(der[0]) 
            der.pop(0) 
    while izq: 
        resultado.append(izq[0]) 
        izq.pop(0) 
    
    while der: 
        resultado.append(der[0]) 
        der.pop(0) 
    
    return resultado 

def mergesort(lista): 
    if len(lista) == 1: 
        return lista 
    mitad = len(lista) // 2 
    izquierda = lista[:mitad] 
    derecha = lista[mitad:] 
    izquierda = mergesort(izquierda) 
    derecha = mergesort(derecha) 
    return merge(izquierda, derecha) 

numeros = [56, 10, 52, 80, 49, 16] 
print("Lista original:") 
print(numeros) 
ordenada = mergesort(numeros) 
print("Lista ordenada:") 
print(ordenada)