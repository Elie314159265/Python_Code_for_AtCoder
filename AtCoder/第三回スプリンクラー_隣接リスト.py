# -*- coding: utf-8 -*-
N,M,Q=map(int,input().split())
graph=[]
#N×0の隣接リストを作る
for i in range(N):
    row=[]
    graph.append(row)
    
#存在する辺を隣接行列に3追加する
for i in range(M): 
    
    #頂点は全部-1しておく
    u,v=map(int,input().split()) 
    u-=1
    v-=1
    
    #隣接リストでは隣接する頂点はこのように記録する。
    graph[u].append(v)
    graph[v].append(u)
    
#各頂点の色を入力
C=list(map(int,input().split()))
for i in range(0,Q):
    query=list(map(int,input().split()))
    if query[0]==1:
        x=query[1]-1
        print(C[x])
        for i in graph[x]:
            C[i]=C[x]
    
    #クエリが２のとき上書き
    if query[0]==2:
        x=query[1]-1
        print(C[x])
        C[x]=query[2]
    