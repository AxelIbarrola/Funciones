# Resuelto sin recursivida

def factorizacion(n):
    
    resultado = n
    
    for i in range(n - 1):
        n -= 1
        resultado *= n
    
    return resultado

print(factorizacion(5))