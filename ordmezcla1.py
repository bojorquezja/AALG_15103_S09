def mezclar(arr): 
    if len(arr) <= 1: 
        return arr 
    mid = len(arr) // 2 
    izquierda = arr[:mid] 
    derecha = arr[mid:] 
    izquierda = mezclar(izquierda) 
    derecha = mezclar(derecha) 
    return fusionar(izquierda, derecha) 

def fusionar(izquierda, derecha): 
    resultado = [] 
    while izquierda and derecha: 
        if izquierda[0] > derecha[0]: 
            resultado.append(derecha[0]) 
            derecha.pop(0) 
        else: 
            resultado.append(izquierda[0])
            izquierda.pop(0) 
    
    while izquierda: 
        resultado.append(izquierda[0]) 
        izquierda.pop(0) 
    
    while derecha: 
        resultado.append(derecha[0]) 
        derecha.pop(0) 
    
    return resultado 

numeros= [20, 40, 36, 120, 80, 19, 62, 24] 
resultado = mezclar(numeros) 
print("Ordenado:", resultado)