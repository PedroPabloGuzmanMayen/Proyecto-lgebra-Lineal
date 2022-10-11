import numpy as np

main_Array = np.array([
    [1,1,1,3,1,1,0],
    [0,2,3,-1,2,3,1],
    [3,2,1,0,1,2,3],
    [1,-1,-2,2,-3,2,1],
    [2,3,-1,-2,-3,-1,1],
    [1,1,3,-3,3,2,0],
    [-2,2,3,0,1,-1,2]
   ]) 

print(round(np.linalg.det(main_Array)))
print()
'''
for i in range(7):
    print("Entradas del renglon" + str(i+1))
    for j in range(7):
        print("Entrada: " + str(i+1) + "," + " " + str(j+1))
        entrada = int(input())
        main_Array[i,j] = entrada

'''

a0 = np.array([
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1]
])


a2 = np.array([
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    
    ])
a3 = np.array([
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
])

a4 = np.array([
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    
])

a5 = np.array([
    [0,0,0],
    [0,0,0],
    [0,0,0]
    
])

a6 = np.array([
    [0,0],
    [0,0]
    ])
a7 = np.array([
    [0]
])

#Generar matrices 2x2 de cada matriz
def generateSubMatrix(Determinant, Matrix,divide, rango):
    pass
    for i in range(rango):
        for j in range(rango):
            Matrix[i,j] = ((Determinant[i,j]*Determinant[i+1,j+1] - Determinant[i+1,j]*Determinant[i,j+1])/divide[i+1,j+1])
            

