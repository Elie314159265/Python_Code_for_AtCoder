# -*- coding: utf-8 -*-
import bisect

n, s = map(int, input().split())
a = list(map(int, input().split()))

#配列aを二回繰り返すように拡張している,つまりlen(a)=2nとなる
#連続する部分和を考える際有効なアルゴリズムである
#aの配列の要素を循環的に扱えるようになる。
for i in range(n):
    a.append(a[i])

#sum_aは累積和を保存するリスト 長さは2n+1となる
sum_a = [0] * (2 * n + 1)
for i in range(2 * n):
    sum_a[i + 1] = sum_a[i] + a[i]

result = False
s %= sum_a[n]
for i in range(2 * n):
    it = bisect.bisect_left(sum_a, sum_a[i] + s)
    if it < 2 * n and sum_a[it] == sum_a[i] + s:
        result = True

print("Yes" if result else "No")