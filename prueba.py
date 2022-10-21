import numpy as np
a = np.array([
    [1,0,2],
    [2,3,4],
    [5,0,6]
    
])

a = np.trim_zeros(a)

print(a)