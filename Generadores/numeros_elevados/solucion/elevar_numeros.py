# Usando funcion generadora

def elevar_al_cuadrado(limite):
    for numero in range(limite):
        yield numero ** 2

resultado = list(elevar_al_cuadrado(100))
print(resultado)

# Usando expresion generadora

numeros_elevados = list(numero ** 2 for numero in range(100))
print(numeros_elevados)