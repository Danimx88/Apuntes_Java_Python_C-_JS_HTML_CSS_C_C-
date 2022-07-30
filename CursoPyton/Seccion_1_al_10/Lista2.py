#definir una lista de tipo Str
nombre = ['Daniel' ,'Omar' ,'Romero' ,'Reyes']
#imprimir la lista nombres
print(nombre)
## accder a los elementos de una lista
print(nombre[0])
print(nombre[2])
print(nombre[-2])
# imprimir un rango
print(nombre[0:2]) # sin incluir el indice 2
#ir del inicio de la lista al inidice (sin incluir)
print(nombre[:3])
#dese el indide indicado hasta al final
print(nombre[1:]) ##solo se pone : ya que nos vamos hasta el ultimo de la lista
##cambiar un valor
nombre[3] = 'Ivone'
print(nombre)
# iterar una lista
for nombres in nombre:
    print(nombres)
else:
    print('No existen mas nombres en la lista')

