# def mi_Funcion(a:int = 10, b:int = 10) -> int:
def mi_Funcion(a = 10, b = 10):
    return a*b
mult =mi_Funcion()
print(f'El valor de la multipliacacion de los valores por defecto es: {mult}')
