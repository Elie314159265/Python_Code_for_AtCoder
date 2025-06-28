# -*- coding: utf-8 -*-
point = list(map(int, input().split()))
# ソートのために配点をすべて -1 倍しておく
point = [-p for p in point]
standings = []
for bit in range(1, 32):
    solved_point = 0
    name = ""
    for digit in range(5):
        # digit 桁めのビットが立っているのが digit 問目を解いた人
        if bit & 1 << digit:
            # 得点と名前にその問題を追加
            solved_point += point[digit]
            name += "ABCDE"[digit]
    # 得点と名前の情報を追加
    standings.append((solved_point, name))
# 順番に並べ替え、名前を順に出力
for _, name in sorted(standings):
    print(name)