'''Escribir un programa en Python para calcular el total a pagar
en una factura de 3 productos , incluyendo IVA,
Al finalizar se debe mostrar los nombres de cada prodcuto;
el valor a pagar por cada uno de ellos  y el total de la factura. '''

print('Ingrese el nombre del primer producto: ')
p1 = input()
print('Cantidad comprada de ',p1)
p1_cant = int(input())
print('Valor de la unidad de ',p1)
p1_uv = int(input())

print('Ingrese el nombre del segundo producto: ')
p2 = input()
print('Cantidad comprada de ',p2)
p2_cant = int(input())
print('Valor de la unidad de ',p2)
p2_uv = int(input())

print('Ingrese el nombre del tercer producto: ')
p3 = input()
print('Cantidad comprada de ',p3)
p3_cant = int(input())
print('Valor de la unidad de ',p3)
p3_uv = int(input())

p1_st = p1_cant * p1_uv
p2_st = p2_cant * p2_uv
p3_st = p3_cant * p3_uv

subTotal = p1_st + p2_st + p3_st
IVA = subTotal * 0.16
Total = subTotal + IVA

print("El total a pagar por ",p1, ' es: ', p1_st)
print("El total a pagar por ",p2, ' es: ', p2_st)
print("El total a pagar por ",p3, ' es: ', p3_st)
print(f"El subtotal de la factura es: {subTotal}")
print(f"El IVA fue: {IVA}")
print(f"El total a pagar con IVA es: {Total}")

