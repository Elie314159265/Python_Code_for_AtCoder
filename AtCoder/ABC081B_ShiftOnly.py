# -*- coding: utf-8 -*-
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
