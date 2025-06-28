# -*- coding: utf-8 -*-
X=int(input())
A=[]
row=[]
for i in range(0,9):
    for j in range(0,9):
        row.append((i+1)*(j+1))
    A.append(row)
    row=[]
sum=0
for i in range(0,9):
    for j in range(0,9):
        if A[i][j]!=X:
            sum+=A[i][j]

print(sum)