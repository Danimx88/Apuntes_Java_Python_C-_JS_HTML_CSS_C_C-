# SVM

# Importamos las bibliotecas
from contextlib import redirect_stderr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import itertools
from matplotlib.colors import ListedColormap

##########################################

# Funcion para mostrar la matriz de confusion
# Pasamos la matriz y el nombre de las clases que tenemos
def MostrarMC(matrizC, clases):

    # Mostramos los datos
    print(matrizC)
    print('Verdaderos negativos', matrizC[0,0])
    print('Verdaderos positivos',matrizC[1,1])
    print('Falsos negativos',matrizC[0,1])
    print('Falsos positivos', matrizC[1,0])
    print('Datos predecidos correctamente',matrizC[0,0]+matrizC[1,1] )
    print('Datos predecidos erroneamente',matrizC[0,1]+matrizC[1,0] )
    print('La precision del modelo es ', matrizC[1,1]/(matrizC[1,1]+matrizC[0,1]))
    print('El recall del modelo es ', matrizC[1,1]/(matrizC[1,1]+matrizC[1,0]))

    #Creamos la cuadricula y la barra
    plt.imshow(matrizC, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Matriz de Confusion')
    plt.colorbar()
    ticks = np.arange(len(clases))
    plt.xticks(ticks, clases)
    plt.yticks(ticks, clases)
    valorMedio = matrizC.max() / 2.
    
    # Colocamos los valores en los cuadros
    for n, m in itertools.product(range(matrizC.shape[0]), range(matrizC.shape[1])):      
        # Colocamos el color del texto segun el valor en la matriz
        if (matrizC[n, m] > valorMedio):
            color='white'
        else:
            color='black'
        plt.text(m, n, format(matrizC[n, m], '.2f' ), horizontalalignment="center",color= color)

    plt.tight_layout()
    plt.ylabel('Valores Actuales')
    plt.xlabel('Valores Predecidos')
    plt.show()

############################################
def MuestraRegresion(X, y, clasif, titulo):
    # Creamos los arreglos para la malla
    X1, X2 = np.meshgrid(np.arange(start = X[:, 0].min() - 1, stop = X[:, 0].max() + 1, step = 0.01),
                         np.arange(start = X[:, 1].min() - 1, stop = X[:, 1].max() + 1, step = 0.01))
    
    # Hacemos la grafica de contorno para cada punto de la malla con el valor de prediccion
    plt.contourf(X1, X2, clasif.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                 alpha = 0.5, cmap = ListedColormap(('red', 'green')))
    plt.xlim(X1.min(), X1.max())
    plt.ylim(X2.min(), X2.max())
    
    for i, j in enumerate(np.unique(y)):
        if(i==0):
            miColor='red'
        else:
            miColor='green'
        
        # Dibujamos el dato
        plt.scatter(X[y== j, 0], X[y == j, 1], c =miColor, label = j)
        
    plt.title(titulo)
    plt.xlabel('mg antibiotico')
    plt.ylabel('Lumenes UV')
    plt.legend()
    plt.show() 
    
############################################

# Leemos y separamos el dataset
dataset = pd.read_csv('BacteriasData.csv')
#dataset = dataset.sort_values("mg")
# 90-200
#dataset = dataset.sort_values("UV_Lumens")
#17400-130518
X = dataset.iloc[:, [0,1]].values
Y = dataset.iloc[:, 2].values

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X,Y, test_size=0.3, random_state = 40)

print(Xtest.shape)
# Hacemos escalamiento de las caracteristicas
from sklearn.preprocessing import StandardScaler

escalador = StandardScaler()
Xtrain = escalador.fit_transform(Xtrain)
Xtest = escalador.transform(Xtest)

# Visualizamos datos
dataset['Eliminado'].value_counts()
import seaborn as sns
sns.countplot(x='Eliminado',data=dataset)
plt.show()

from sklearn.svm import SVC
clasificador = SVC(kernel = 'rbf',random_state = 40) 
clasificador.fit(Xtrain, Ytrain)

# Hacemos la prediccion de los elementos en la seccion del test
Ypred = clasificador.predict(Xtest)

# Creamos la matriz de confusion
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Ytest,Ypred)

MostrarMC(cm,['No Eliminado','Eliminado'])
# Mostramos los datasets y las regiones de prediccion

MuestraRegresion(Xtrain, Ytrain, clasificador, 'Entrenamiento')
MuestraRegresion(Xtest,Ytest, clasificador, 'Prueba')

# Calculamoms y mostramos la precision
from sklearn.metrics import precision_score

precision=precision_score(Ytest,Ypred)
print('La precision del modelo es ', precision )


import random
Lista = []
Numeros = int(input("Cuantos numeros de prueba deseas generar: "))
for i in range(Numeros):
    A = random.uniform(90, 200)
    B = random.uniform(17400, 130518)
    Lista.append([A,B])
print(Lista)    

X_nueva = escalador.transform(Lista)
y_nueva = clasificador.predict(X_nueva)
MuestraRegresion(X_nueva,y_nueva, clasificador, 'Nuevo')

#Z = escalador.transform(Z)
#Ynueva = clasificador.predict(Z)
#MuestraRegresion(Z,Ynueva, clasificador, 'Nuevo')
#print(Ynueva)
#Xnueva= [[90.6794, 69595]]
#Xnueva= np.array([[100.13,40000]])
#Z = np.array(dataset.iloc[:5, [0,1]].values)
