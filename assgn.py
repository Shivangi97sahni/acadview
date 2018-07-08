#1
import numpy as np
array = np.random.rand(10, 1)
print(array)
print(array.mean())


#2
import numpy as np
array = np.random.rand(20,1)
print(array)
variance = array.std()
standard_deviation = (array - array.mean())/variance

print("Variance : {} \n\nStandard Deviation : \n {}".format(variance, standard_deviation))


#3
import numpy as np
A = np.random.rand(10,20)
B = np.random.rand(20,25)
print(A)
print("\n")
print(B)
print("\n")
matrix_mul = np.matmul(A,B)
print(matrix_mul)


#4
import numpy as np
a = np.random.rand(10, 1)
print(a)

def func(x):
    return (1 / (1 + np.exp(-x)))


result = np.apply_along_axis(func, 0, a)


print( result)