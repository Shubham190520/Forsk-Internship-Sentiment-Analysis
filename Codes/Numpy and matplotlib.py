
list1 = [1,2,3,4,5,6,7,8,9,10]

list2 = list1*10

list4 = []

for item in list1:
    list4.append(item*10)
          #OR
          
[item*10 for item in list1] #LISTCOMPREHENSION

list1 = [1,2,3,4,5,6,7,8,9,10]

import numpy as np

 x = np.array(list1)
 
 x*10
 
 list1 = [1,2,3,4,5,6,7,8,9]
 
 x = np.array(list1)
 
 x = x.reshape(3,3)
 
 x = np.arange(5)
 
 x = np.arange(5, dtype = 'uint8')
 
 np.zeros((2,3))
 
 np.ones((4,3))
 
 -----------------------------
 
 import matplotlib.pyplot as plt
 
 x = [1,2,3,4,5]
 
 y = [1,8,27,64,125]
 
 plt.scatter(x,y)
 
 plt.plot(x,y, color = 'green')
 
 plt.plot(x,y)