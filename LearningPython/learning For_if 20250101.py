# -*- coding: utf-8 -*-
#learning if , for
prefecture = "東京"
if prefecture =="東京":
    print("日本の首都です")
elif prefecture=="ワシントン":
    print("アメリカの首都です")
else :
    print("該当しません")
    
number =10001
if number%2 ==0:
    print("偶数である")
else :
    print("奇数である")


#learing for 
#for 変数 in 繰り返しオブジェクト:
#    繰り返したい処理
#が基本的な繰り返し文。　繰り返しオブジェクトはリスト、辞書、タプル、集合などである。
scores=[90,30,49,50,60,70]
for x in scores:
    print(x)
    print(x/2)

#辞書を使ったfor文の構文
#for 変数１、変数２　in 辞書.items():
#    繰り返す処理
#変数1はKeyであり、変数２はValueである。
fruits={"apple":130,
        "banana":200,
        "lemon":400}
for name,price in fruits.items():
    print(f"{name}は{price}円です")

#rangeとは連続した整数を取り出すことができる
#breakはfor自体抜ける。continueは後続処理をスキップする場合に使用。
for x in range(5):
    print(x)
for x in range(1,100):
    if x>30:
        break
    if x%2 ==0:
        continue
    print(x)

#練習問題
#うるう年を判別せよ。ただし、うるう年とは4で割り切れるかつ100で割り切れない年。ただし、400で割り切れるなら例外としてうるう年
year=2025
if (year%4==0 and year%100!=0) or year%400==0:
    print(f"{year}年はうるう年である")
else :
    print(f"{year}年は平年です")
    


#練習問題（FizzBuzz問題）
#１～１００までの数字を出力させるプログラムを作る。
#３の倍数のときFizz、5の倍数の時Buzz,15の倍数の時FizzBuzzと数字の代わりに表示させる。
for x in range(1,101):
    if x%15==0:
        print("FizzBuzz")
    elif x%5==0:
        print("Buzz")
    elif x%3==0:
        print("Fizz")
    else :
        print(x)
        



