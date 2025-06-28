# -*- coding: utf-8 -*-
N,D=map(int,input().split())
TLlist=[]
for i in range(N):
    row=[]
    row=list(map(int,input().split()))
    TLlist.append(row)
max_result=[]
for i in range(1,D+1):
    result=[]
    for j in range(0,N):
        result.append(TLlist[j][0]*(TLlist[j][1]+i))
    max_result.append(max(result))
for i in range(D):
    print(max_result[i])