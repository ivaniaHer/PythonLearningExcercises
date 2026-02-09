from scipy import io
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Export
io.savemat('arr2.mat',{"vec":arr})
# Import
mydata = io.loadmat('arr2.mat')
print(mydata)
print(mydata['vec'])
