# calculate mean square error MSE
import numpy as np
O =[ 7, 5, 2, 0, 1, 8]
F = [ 6, 5, 0, -1, 0, 7]

sum =0
for i in range(len(O)):
    sum = sum+(F[i]-O[i])**2
mse = sum /len(O)
print(mse)

# another solution
MSE = np.square(np.subtract(O,F)).mean()
print(MSE)



