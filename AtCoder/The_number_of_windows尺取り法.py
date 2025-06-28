# -*- coding: utf-8 -*-
def count_valid_intervals(N, A, Q, queries):
    results = []
    
    for x in queries:
        l, r = 0, 0
        current_sum = 0
        count = 0
        #左端を進める
        while l < N:
            # 右端をすすめる
            while r < N and current_sum + A[r] <= x:
                current_sum += A[r]
                r += 1
            
            # 条件を満たす区間の個数を加算
            count += (r - l)
            
            # 左端を進める
            current_sum -= A[l]
            l += 1
        
        results.append(count)
    
    return results

# 入力処理
N,Q = map(int,(input().split()))
A = list(map(int, input().split()))
queries =list(map(int,input().split()))

# 処理と出力
results = count_valid_intervals(N, A, Q, queries)
for res in results:
    print(res)