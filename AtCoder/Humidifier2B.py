# -*- coding: utf-8 -*-
N=int(input())
TVlist=[]
for i in range(N):
    row=[]
    row=list(map(int,input().split()))
    TVlist.append(row)

sumV=TVlist[0][1]
for i in range(1,N):
    sumV=sumV-(TVlist[i][0]-TVlist[i-1][0])
    if sumV<=0:
        sumV=0
    sumV=sumV+TVlist[i][1]
print(sumV)