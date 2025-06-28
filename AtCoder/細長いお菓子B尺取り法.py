# -*- coding: utf-8 -*-
def max_unique_length(N, A):
    seen = {}  # 現在の区間内の味のカウント
    l = 0  # 左端
    max_length = 0  # 最大長

    #右端を進めるループ
    for r in range(N):
        # 味 A[r] を区間に追加
        if A[r] in seen:
            seen[A[r]] += 1
        else:
            seen[A[r]] = 1
        
        # 条件を満たさなくなったら左端を進める
        while seen[A[r]] > 1:
            seen[A[l]] -= 1
            if seen[A[l]] == 0:
                #出現回数が0になった要素を辞書から削除
                del seen[A[l]]  # 味 A[l] を区間から削除
            l += 1
        
        # 条件を満たす区間の長さを更新
        max_length = max(max_length, r - l + 1)
    
    return max_length

# 入力処理
N = int(input())
A = list(map(int, input().split()))

# 結果を出力
print(max_unique_length(N, A))