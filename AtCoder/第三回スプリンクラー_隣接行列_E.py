# -*- coding: utf-8 -*-
N,M,Q=map(int,input().split())
graph=[]
#N×Nの隣接行列を作る
for i in range(N):
    row=[]
    for j in range(N):
        row.append(False)
    graph.append(row)
    
for i in range(M):#存在する辺を隣接行列に3追加する
    u,v=map(int,input().split())#頂点は全部-1しておく
    u-=1
    v-=1
    graph[u][v]=True
    graph[v][u]=True

C=list(map(int,input().split()))#各頂点の色を入力
for i in range(0,Q):
    query=list(map(int,input().split()))
    if query[0]==1:
        x=query[1]-1
        print(C[x])
        for i in range(0,N):#隣接するグラフがあれば隣接する頂点の色を塗る
            if graph[x][i]:
                C[i]=C[x]
    if query[0]==2:#クエリが２のとき上書き
        x=query[1]-1
        print(C[x])
        C[x]=query[2]
    