# -*- coding: utf-8 -*-
def count_increasing_subarrays(N, A):
    l, count = 0, 0
    #尺取り法では右端をすすめながら条件を満たす区間を探索
    for r in range(1, N):
        # 条件を満たす間、右端を進める
        #単調増加でない場合、左端を更新
        if A[r - 1] >= A[r]:
            l = r  # 左端を更新
            
        
        # 条件を満たす区間の個数を加算
        #(l,r),(l+1,r),(l+2,r),…,(r,r)は区間を満たす数
        count += (r - l + 1)
    
    return count

# 入力処理
N = int(input())
A = list(map(int, input().split()))

# 結果を出力
print(count_increasing_subarrays(N, A)+1)