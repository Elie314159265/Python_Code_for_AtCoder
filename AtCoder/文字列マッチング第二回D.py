# -*- coding: utf-8 -*-
#文字列Tが文字列Sにマッチするかどうかを判定する関数
#マッチするときはTrue,マッチしない時はFalse
def is_match(S,T):
    for i in range(0,len(S)-len(T)+1):
        ok=True
        for j in range(len(T)):
            if S[i+j]!=T[j] and T[j]!='.':
                ok=False
        if ok:
            return True
    return False

S=input()
C="abcdefghijkmlnopqrstuvwxyg."
M=[]
#一文字のみの場合
for T in C:
    if is_match(S,T):
        M.append(T)
#二文字のみの場合
for c1 in C:
    for c2 in C:
        T=c1+c2
        if is_match(S,T):
            M.append(T)
#三文字のみの場合
#アルファベットは27文字より、28^3回ループを回す 一秒かからない
for c1 in C:
    for c2 in C:
        for c3 in C:
            T=c1+c2+c3
            if is_match(S,T):
                M.append(T)
print(len(M))