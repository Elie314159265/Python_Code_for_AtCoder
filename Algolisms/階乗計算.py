# -*- coding: utf-8 -*-
#階乗計算
def fact_rec(n):
    if n==1:
        return 1
    else :
        return (n*fact_rec(n-1))
#調和級数
def fact_r(n):
    if n==1:
        return 1
    else : 
        return (1/n + fact_r(n-1))

N=int(input())
print(fact_rec(N))
print(fact_r(N))
