# -*- coding: utf-8 -*-
# Learning List
#なぜリストを使う？＞データを扱いやすくするため。追加や削除の容易化、つまり管理の容易化。
studentNumber=[1,2,3,4,5]
print(studentNumber[0])
print(studentNumber[-1])
passStudent=studentNumber[1:5]
print(passStudent)
studentNumber.append(6)
studentNumber.append(7)
print(studentNumber)

#一番大きい値を取得
maxnumber=max(studentNumber)
print(maxnumber)

#昇順、降順に並び替え
sortednumber=sorted(studentNumber)
print(sortednumber)
sortednumber=sorted(studentNumber, reverse=True)
print(sortednumber)