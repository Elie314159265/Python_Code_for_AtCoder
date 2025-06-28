# -*- coding: utf-8 -*-
cnt=0
def fib(n,cnt):
    if n==0 or n==1:
        return 1
    elif n==5:
        cnt+=1
        return fib(n-1)+fib(n-2)
    else :
        return fib(n-1)+fib(n-2)


n=int(input())
print(fib(n))
