# -*- coding: utf-8 -*-
number_sum=0
for x in range(2,1000):
    cnt=0
    for number in range(2,x):
        if x%(number)==0:
            cnt+=1
    if cnt==0:
        number_sum+=x
    
print(f"1～1000までの素数の合計は{number_sum}である")