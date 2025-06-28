# -*- coding: utf-8 -*-
N=int(input("N(1~100)"))
di=list(map(int,input("di(1~100)").split()))
di=sorted(di)
cnt=0
for i in range(0,N-1,1):
    if di[i]==di[i+1]:
        cnt+=1
print(N-cnt)