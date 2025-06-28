# -*- coding: utf-8 -*-
#Learnig 尺取り法
#簡単に言うと、条件を満たすような区間を全て求めることができる。
#O(n²)をO(n)に改善することができる。
#①条件を満たす限り、右端を進める
#②条件を満たさなくなったら左端を条件を満たすまで進める。

"""
問題文
長さ 
N の非負整数列 Sと整数 K があります。 あなたの仕事は、以下の条件を満たす 
S の 連続する 部分列のうち、最も長いものの長さを求めることです。部分列の長さは 
1 以上の列でないといけません。

その部分列に含まれる全ての要素の値の積は、
K 以下である。
もし条件を満足す部分列が一つも存在しない時は、0を出力すること
"""

n,k = map(int,input().split())
s = [int(input()) for i in range(n)]

if 0 in s:
    print(n)
else:
    right, ans, tmp = 0, 0, 1
    #左端leftを0～n-1まで動かす
    for left in range(n):
        #右端rightを延ばす
        while right< n and tmp*s[right] <= k:
            tmp *= s[right]
            right+= 1
        #現在の部分列の長さright-leftを最大値として記録
        ans = max(ans,right-left)
        #左端を進める処理
        #left==rightのとき部分列が空になるので右端を進める。
        if left == right:
            right+= 1
        else:
            #通常ケースでは左端を進めるので部分列の積からs[left]を除外
            tmp //= s[left]
    print(ans)