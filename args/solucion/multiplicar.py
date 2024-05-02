def multiplicar(*numeros):
    resultado = 1
    
    for numero in numeros:
        resultado *= numero
    
    return resultado

print(multiplicar(3, 4, 5, 6))