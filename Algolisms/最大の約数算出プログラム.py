# -*- coding: utf-8 -*-
x=int(input("その数の最大の約数を求めます(3以上100)"))
biggest_divisor=None
for guess in range(3,x):
    if x%guess==0:
        biggest_divisor=guess

if biggest_divisor==None:
    print("素数です（prime number）")
else :
    print(f"{biggest_divisor}です")