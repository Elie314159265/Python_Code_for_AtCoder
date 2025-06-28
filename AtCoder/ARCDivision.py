# -*- coding: utf-8 -*-
N,R=map(int,input().split())

N_2list=[]
for i in range(0,N):
    row=[]
    row=list(map(int,input().split()))
    N_2list.append(row)

T=R
for i in range(0,N):
    if 1600<=T<=2799 and N_2list[i][0]==1:
        T=T+N_2list[i][1]
    if 1200<=T<=2399 and N_2list[i][0]==2:
        T=T+N_2list[i][1]
print(T)