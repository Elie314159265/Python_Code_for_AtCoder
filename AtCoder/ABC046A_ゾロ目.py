# -*- coding: utf-8 -*-
import math
N=int(input())

x=math.ceil(N/9)#Nを9で割り、小数点以下を切り上げる。桁数を求める。
y=N%9
if y==0:
    y=9

ans=""
for _ in range(0,x):
    ans+=str(y)

print(ans)