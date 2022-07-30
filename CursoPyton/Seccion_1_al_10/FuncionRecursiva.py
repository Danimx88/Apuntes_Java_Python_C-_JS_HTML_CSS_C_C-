# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120
def factorial(numero): #Define la funcion llamada factor(valor a factorizar)
    if numero == 1: #si valor a factorizar es = 1
        return 1 #Entonces retorna 1 porque el factor de 1 es = 1
    else: #Sino
        return numero * factorial(numero-1) # multiplica variable numero por funcion(variable-1) hasta llegar al 1 de return
    ##Funcion recursiva mandar a llamar a si misma

numero = int(input('Ingrese el valor a factorizar: ')) #ingresa el valor de numero
resultado = factorial(numero) #resultado tendra el valor de la funcion factorial
print(f'El factorial de {numero} es {resultado}') # imprime el valor
