# -*- coding: utf-8 -*-
#黒板に 
#N個の正の整数 A1,A2,.....An
#が書かれています。
#すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます。

#黒板に書かれている整数すべてを，2
#で割ったものに置き換える。
#すぬけ君は最大で何回操作を行うことができるかを求めてください。
Nlist=list(map(int,input().split()))
Nlist=sorted(Nlist)
divisor=2
cnt=0
evenCnt=0
if cnt==0:
    while(Nlist[0]%2==0 and Nlist[1]%2==0 and Nlist[2]%2==0):
        if Nlist[0]%2==0 and Nlist[1]%2==0 and Nlist[2]%2==0:
            Nlist[0]=Nlist[0]/2
            Nlist[1]=Nlist[1]/2
            Nlist[2]=Nlist[2]/2
            evenCnt+=1
            
print(f"{evenCnt}回操作を行うことができる")