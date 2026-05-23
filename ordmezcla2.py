def ordMezcla(lista): 
    if len(lista) == 1: 
        return lista 
    
    mitad = len(lista) // 2 
    izq = lista[:mitad] 
    der = lista[mitad:] 
    izq = ordMezcla(izq) 
    der = ordMezcla(der)
     
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

numeros = [56, 10, 52, 80, 49, 16] 
print("Lista original:") 
print(numeros) 
ordenada = ordMezcla(numeros) 
print("Lista ordenada:") 
print(ordenada)