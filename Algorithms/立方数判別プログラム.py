# -*- coding: utf-8 -*-
x=int(input("立方数かどうか判別する値を入力してください:"))
ans=0
while ans**3<abs(x):
    ans+=1

if ans**3 != abs(x):
    print("立方数ではない")
else:
    print("立方数である")