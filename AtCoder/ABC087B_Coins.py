# -*- coding: utf-8 -*-
A=int(input("A:"))
B=int(input("B:"))
C=int(input("C:"))
X=int(input("X:"))
res,total=0,0
a,b,c=0,0,0
cnt=0
for a in range(0,A+1,1):
    for b in range(0,B+1,1):
        for c in range(0,C+1,1):
            total=500*a+100*b+50*c
            if total==X:
                res+=1
print(res)