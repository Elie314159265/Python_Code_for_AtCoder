# -*- coding: utf-8 -*-
#my code
"""
import bisect
N = int(input())
A = list(map(int, input().split()))

cnt = 0
for i in range(N):
    threshold = 2 * A[i]
    j= bisect.bisect_left(A, threshold, lo=i + 1)
    cnt += N - j  

print(cnt)
"""
#解説　尺取り法
N=int(input())
A=list(map(int,input().split()))
ans=0
left=0
for right in A:
    while left<N and A[left]*2<=right:
        left+=1
    ans+=left
print(ans)