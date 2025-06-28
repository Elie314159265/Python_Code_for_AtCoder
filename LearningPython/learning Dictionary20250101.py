# -*- coding: utf-8 -*-
#Learning Dictionary
#辞書はKeyとValueのセット Keyの重複は許されない！！
#簡単に言うと、リストの値に名前を付けたもの
scores={"math":99,
        "japanese":77,
        "English":98}
print(scores)

#要素数を求める
number=len(scores)
print(number)

#辞書からValueのみ抜き出す
scoreValue=list(scores.values())
print(scoreValue)

#辞書からKeyのみ抜き出す
scoreKey=list(scores.keys())
print(scoreKey)

#練習問題
#5教科のテストにおいて理科は社会より何点高いかを[〇点]という文字で出力するプログラムを組む
scores={"math":82,
        "japanese":74,
        "English":60,
        "science":92,
        "society":70}
science_Minus_society=scores["science"]-scores["society"]
print(f"理科は社会より{science_Minus_society}点高い")

#練習問題
#5教科のテストをリストで表した時平均点を出力するプログラムを作成せよ
scorelist=list(scores.values())
ave=sum(scorelist)/len(scorelist)
print(f"平均点は{ave}点")