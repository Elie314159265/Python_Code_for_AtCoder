# -*- coding: utf-8 -*-
N=int(input("N:"))
A=int(input("A:"))
B=int(input("B:"))

def findsumdigits(n):
    sum=0
    while(n>0):
        sum+=n%10
        n=int(n/10)
    return sum

sum1=0
sum2=0
cnt=1
for cnt in range(1,N+1,1):
    sum1=findsumdigits(cnt)
    if sum1>=A and sum1<=B:
        sum2+=cnt
    sum1=0
print(sum2)
    