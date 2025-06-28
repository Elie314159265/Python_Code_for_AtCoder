# -*- coding: utf-8 -*-
K=int(input())
A,B=map(int,input().split())
ok=False
i=1
"""
for i in range(A,B+1):#全探索
    if i%K==0:
        ok=True
if ok:
    print("OK")
else:
    print("NG")
"""
while(i*K<=B):
    if A <= i*K <= B:#Kの倍数のみ調べる
        ok=True
    i+=1
if ok:
    print("OK")
else:
    print("NG")