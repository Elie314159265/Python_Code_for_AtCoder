# -*- coding: utf-8 -*-
"""
import numpy
arr=numpy.array([0,1,2,3,4,5,6,7,8,9])
print(arr)


for i in range(10):
    arr[i]=arr[i]+5
print(arr)
    

arr1=numpy.array([[1,0,0],[0,1,0],[0,0,1]])
print(arr1)

data = [13, 29, 35, 48, 55, 61, 72]

datanumpy=numpy.array(data)
sum=0
max=0
min=9999
for i in range(7):
    sum+=datanumpy[i]
    if max < datanumpy[i]:
        max=datanumpy[i]
    if min > datanumpy[i]:
        min=datanumpy[i]
ave=sum/7
print(f"average:{ave}, sum:{sum}, max:{max}, min{min}")

arr2=numpy.arange(1,21)
arr3=[]
for i in range(20):
    if (i+1) % 2 ==0:
        arr3.append(arr2[i])
print(arr3)

sum1=0
arr = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for i in range(3):
    for j in range(3):
        sum1+=arr[i][j]
        
total_sum=numpy.sum(arr)
print(f"全体の合計:{total_sum}")
row_means=numpy.mean(arr,axis=1)
print(f"各行の平均:{row_means}")
col_sums=numpy.sum(arr,axis=0)
print(f"各列の合計:{col_sums}")

"""
"""
import numpy as np 
arr = np.random.randint(0,100,size=20)
print(f"元の配列:{arr}")

new_arr=arr[arr>=20]
new1_arr=new_arr[new_arr <= 70]
print(new1_arr)


arr = np.array([
    [88, 92, 79],
    [95, 90, 93],
    [70, 85, 88]
])
ave=np.mean(arr,axis=0)
print(ave)
"""
import numpy as np

scores = np.array([72, 85, 90, 78, 88, 91, 67, 80, 76, 95])
ave=np.mean(scores)
var=np.var(scores)
std=np.std(scores)
print(f"ave:{ave} var:{var} std:{std}")