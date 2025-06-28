# -*- coding: utf-8 -*-
N=int(input())
S=[]
for _ in range(0,N,1):
    si=input()#空白も一要素として数えられることに注意
    si=list(si)#リストにしないと書き換えができない
    S.append(si)
for i in range(N-2,-1,-1):
    for j in range(1,2*N-2):
        """if (S[i+1][j-1]=="X" or S[i+1][j]=="X" or S[i+1][j+1]=="X") and S[i][j]=="#":
            S[i][j]="X"
            """
        if S[i][j]=='1':
            if S[i+1][j-1]=='2':
                S[i][j]='2'
            if S[i+1][j]=='2':
                S[i][j]='2'
            if S[i+1][j+1]=='2':
                S[i][j]='2'
        
        
for i in range(0,N):#Sをリストから文字列に変換して出力
    S[i]=''.join(S[i])
    print(S[i])
