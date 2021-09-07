#From the below array, retrieve the values([[3,4],[5,6]]) using indexing

import numpy as np
lst1 = [1,2,3,4,5]
lst2 = [2,3,4,5,6]
lst3 = [4,5,6,7,8]

arr1 = np.array([lst1, lst2, lst3])
print(arr1[1:,1:3])