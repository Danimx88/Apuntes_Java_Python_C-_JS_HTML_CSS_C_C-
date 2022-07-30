#Definir tupla
##Las tuplas ya no permiten modificar, son inmutables
frutas = ('Naranja','Mango','Platano') #trupla entre ()
#saber el rango
print(len(frutas))
#acceder a un elemento en particular
#print(frutas[0])
print(frutas[2])
print(frutas[-2])
print(frutas[0:1])

for fruta in frutas:
    print(fruta, end=' ') #end=' ' agrega un espacio para que no se salten las lineas

# frutas[1] = 'pera'  ----> no deja modificar porque es una trupla

frutasLista = list(frutas) ##convierte una trupla a una lista
frutasLista[0] = 'Uva' #Modifica el valor 0 por Uva
frutas = tuple(frutasLista) #tuple que es tupla, cambia frutaLista por trupla ya que se cambio el valor de 0
print('\n', frutas)
# del frutas   ---->no se puede ejecutar este comando porque es una trupla i es inmutable
