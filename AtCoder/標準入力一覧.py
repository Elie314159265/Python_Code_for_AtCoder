# -*- coding: utf-8 -*-
#標準入力一覧

#一行　入力が一つ
a=input()#abc
a=int(input())#12

#入力文字列をリストへ変換
#abcd > ['a','b','c','d']
list_a=list(input())

#文字列をsplitで分割し、リストに格納する。
#一行　入力が複数
#apple lemon grape > ["apple","lemon","grape"]
list_a=input().split()
red,yellow,purple=input().split()

#数字が一行複数入力の場合
#1 2 3 4 > [1,2,3,4]
#mapは（使いたい関数、リスト等）のように使う
list_a=list(map(int,input().split()))

#複数行　入力が各行一つの場合
#3
#apple
#lemon 
#grape
#["apple","lemon","grape"]
n=int(input())
list_a=[input() for i in range(n)]

#複数行　入力が各行一つの場合
#3
#1
#2
#3
#[1,2,3]
n=int(input())
list_a=[int(input()) for i in range(n)]

