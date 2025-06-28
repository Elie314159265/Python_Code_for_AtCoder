# -*- coding: utf-8 -*-
epsilon=0.001
num_guesses=0
low=0
x=int(input("入力した数の平方根を求めます。"))
high=max(1,x)
ans=(high+low)/2
while abs(ans**2-x)>=epsilon:
    print(f"low={low},high={high},ans={ans}")
    num_guesses+=1
    if ans**2<x:
        low=ans
    else:
        high=ans
    ans=(low+high)/2
print(f"num_guesses={num_guesses}")
print(f"{ans}がxの平方根の近似解です(二分法)")