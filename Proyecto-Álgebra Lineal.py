'''
Proyecto de Álgebra Lineal

Pedro Pablo Guzmán Mayen 22111
Gustavo Adolfo Cruz Bardales 22779
Javier Andrés Chen González 22779
José Antonio Mérida Castejón 201105
Luis Fernando Mendoza Álvarez 19644

'''
import numpy as np
import sys
num = int(input("De que tamaño quieres que sea la matriz: "))
while num < 3:
    print("Solo se aceptan matrices qur tengan un tamaño mayor o igual a 3, intenta de nuevo")
    num = int(input("De que tamaño quieres que sea la matriz: "))

#Aquí genera una matriz en base al numero que brindo el usuario
main_array = np.identity(num, int)
#Se crea ina lista que servirá para más adelante
matrix_list = []

#Esta función permite al usuario seleccionar las entradas de la matriz
def matrixIndex(array, number):
    
    for i in range(number):
        print("Entradas del renglon " + str(i+1))
        for j in range(number):
            print("Entrada: " + str(i+1) + "," + " " + str(j+1))
            entrada = int(input())
            main_array[i,j] = entrada
            
            
#Usar la función con las variables del programa
matrixIndex(main_array, num)

#Esta función genera las matrices de distintos tamaños que son importantes para encontrar el determinante mediante el método de condensación (ver el libro)
def generateSubMatrix(lista, numero):
    #Reversed sirve para que el ciclo for empieze "desde atrás"
    for i in reversed(range(numero+2)):
        if i ==0:
            #Romper el ciclo ya que si no se rompe, se va a generar una matriz 0x0, la cuál no sirve
            break;
        #Añadir a la lista una matriz con el tamaño requierido, se usa la función ones la cuál genera matrices cuyas entradas son todas 1
        lista.append(np.ones((i,i), int))

#Usar la función con las variables
generateSubMatrix(matrix_list, num)

#Siempre la matriz 1 de la pirámide (ver libro) debe ser la matriz que ya tenemos, por lo que se cambia el valor 1 de la lista a la matriz brindada por el usuario.
#main_array = main_array+main_array[1,1]
matrix_list[1] = main_array

#Esta función genera el determinante
def genrateDeterminant(lista, numero):
    #Se usa 2 ya que siempre se inicia en la matriz 2 de la pirámide. Este ciclo recorre la lista que tiene las matrices en forma de pirámide
    for i in range (2, numero+1):
        #Recorre cada renglón de la matriz
        for j in range(len(lista[i])):
            #Recorre cada columna de la matriz dada
            for k in range(len(lista[i])):
                #Este if verifica si se divide por 0
                    #np.where(main_array == 0)
                    p = int(lista[i-2][j+1,k+1])
                    if p == 0:
                        #print(main_array+2*main_array[3,3])    
                        a = int(np.linalg.det(main_array))
                        print()
                        print("El determinante de la matriz es: "+str(a))
                        
                        print(main_array)
                        #print("El determinante es: "+str(a))
                        sys.exit(1)
                        break
                        
                    elif p != 0:    
                        #lista[i-2][j+1,k+1] = lista[i-2][j+1,k+1] + lista[i-2][j,k]
                #Se cambia el valor de cada entrada de la matriz dada. 
                        lista[i][j,k] = int(int(lista[i-1][j,k]*lista[i-1][j+1,k+1]-lista[i-1][j+1,k]*lista[i-1][j,k+1])/p)


#Usar la función con las variables
genrateDeterminant(matrix_list, num)
#Dar el resultado
print("El determinante de la matriz es: " + str(int(matrix_list[num][0,0])))
print()
print(main_array)
