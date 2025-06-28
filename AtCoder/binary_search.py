# -*- coding: utf-8 -*-
#二分探索(binary search)
def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

arr=[1,2,3,4,5,6,7,8,9,10]
target=7
result=binary_search(arr,target)
if result !=-1:
    print(f"ターゲット{target}はインデックス{result}にあります")
else:
    print("ターゲットはインデックス中に存在しない")
    
"""

def binary_search(arr,target):
    left,right=0,len(arr-1)
    mid = (left + right)//2
    while left<=right:
        if arr[mid]==target:
            return target
        elif arr[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return -1

"""