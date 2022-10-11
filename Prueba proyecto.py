import numpy as np

main_Array = np.array([
    [2,3,-1,2,0],
    [1,2,3,1,-4],
    [2,-1,2,1,1],
    [3,1,-1,2,-2],
    [-4,1,0,1,2]

])

a0 = np.array([
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]

])




a2 = np.array([
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]


])


a3 = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]


])

a4 = np.array([
    [1,1],
    [1,1]


])

a5 = np.array([
    [1]


])

def generateSubMatrix(Determinant, Matrix,divide, rango):
    pass
    for i in range(rango):
        for j in range(rango):
            Matrix[i,j] = ((Determinant[i,j]*Determinant[i+1,j+1] - Determinant[i+1,j]*Determinant[i,j+1])/divide[i+1,j+1])

generateSubMatrix(main_Array, a2, a0, 4)

print(a2)
print()

generateSubMatrix(a2, a3, main_Array, 3)

print(a3)
print()

#print(a4)
generateSubMatrix(a3,a4,a2,2)

print(a4)

print()

generateSubMatrix(a4,a5,a3,1)

print(a5)
print()