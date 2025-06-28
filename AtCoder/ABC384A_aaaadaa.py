# -*- coding: utf-8 -*-mn
list_a=input().split()
N=int(list_a[0])
c1=list_a[1]
c2=list_a[2]
S=list(input())
for i in range(len(S)):
    if S[i] != c1:
        S[i]=c2
S="".join(S)
print(S)


"""
list_a = input().split()
N = int(list_a[0])
c1 = list_a[1]
c2 = list_a[2]

S = list(input())  # 入力された文字列をリストに変換
for i in range(len(S)):  # 0 から len(S)-1 までループ
    if S[i] != c1:  # 文字が c1 ではない場合
        S[i] = c2  # c2 に置き換え

# リストを文字列に戻して出力
print("".join(S))
"""