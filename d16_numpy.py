import numpy as np

# arr1=np.array([1,2,3,4,5])
# # print(arr1)

# print(type(arr1))

# arr2=np.array([[1,2,3,4],[5,6,7,8]])

# # print(arr2)

# arr3=np.array([
#   [[1,2,3,4],[5,6,7,8]],[[5,6,7,8],[0,9,8,7]]
#   ]) 
# print(arr3)
# print('\n================================')
# # indexing

# print(arr2[0][2])
# print('\n================================')
# print(arr2[1])
# print('\n================================')
# print(arr2[:2])

# # print(arr3[1][1][0:2])



# random

from numpy import random

# arr4=random.randint(50,size=(3,5))

# print(arr4)

# arr5=random.choice([1,2,3,4],size=(3,3),p=(0.3,0.2,0.3,0.2))
# print(arr5)

import matplotlib.pyplot as plt
import seaborn as sns

arr6=[1,2,3,4]

plt.plot(arr6,marker="x")
plt.xlabel("Plotting array elements")
plt.title("py plot lib")
# sns.displot([1,2,3,4])
plt.show()


