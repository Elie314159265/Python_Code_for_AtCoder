# -*- coding: utf-8 -*-
#learning 関数
#関数とは処理をひとまとめにすることができる
#利点はプログラム内に同じ処理が何度も出てくるとき記述を単純にできる

#def 関数名():
#で関数定義できる
#注意！関数定義は呼び出しよりも前に書くこと。
def print_hello():
    print("Hello!")

def add_numbers(a,b):
    c=a+b
    return c

def sub_numbers(a,b):
    c=a-b
    return c

#pythonでは戻り値を2つ以上指定できるので上記関数をひとまとめにすることができる
#ただしこの場合通常タプルを返すが、個々の変数に代入することでタプルではなく変数に代入することもできる
def add_sub_numbers(a,b):
    c=a+b
    d=a-b
    return c,d


print_hello()
added_number=add_numbers(100,10)
sub_number=sub_numbers(100,10)
print(added_number)
print(sub_number)
print(add_sub_numbers(100,10))#タプルで出力
x,y=add_sub_numbers(100, 10)
print(x,y)#変数を出力
