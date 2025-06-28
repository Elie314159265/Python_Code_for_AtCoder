# -*- coding: utf-8 -*-


N=int(input("N(1~2000):"))
Y=int(input("Y(1000~2*10^7,1000の倍数):"))

res10000,res5000,res1000=-1,-1,-1
for a in range(0,N,1):
    for b in range(0,N,1):
        #ここでcもforを回すとN^3で8,000,000,000通り回ってしまう。
        #一秒間でfor文は100,000,000回程度回ることを考えると制限時間をオーバー
        #よってN=a+b+cの関係式を利用 
        c=N-a-b
        total=a*10000+b*5000+c*1000
        if total==Y:
            res10000=a
            res5000=b
            res1000=c
print(res10000,res5000,res1000)