# -*- coding: utf-8 -*-
#learning class
#クラスはプログラムを抽象化できすっきりしたコードにできる！
#例えばマリオカートのカートはクラス化するとオブジェクト化する際記述が見やすくなる。
#class クラス名
#でクラス名を宣言
class User:
    #まずインスタンス変数、メソッドをかく 
    #イニシャライザという処理
    def __init__(self,name,mail_address,point):
        self.name=name
        self.mail_address=mail_address
        self.point=point
        
    def add_point(self,point):#ポイントの付与を行う処理
        #selfはオブジェクトを表す
        self.point=self.point+point
        
User_1=User("佐藤葵","sato@example.com",500)
User2=User("小林ゆい","kobayashi@example.com",1000)
#オブジェクトの取得は　インスタンス名.変数 で行う
print(User_1.name)
User_1.add_point(2000)
print(f"{User_1.name}のポイントは{User_1.point}です")



class Student:
    def __init__(self,name,math,english,japanese,science,society):
        self.name=name
        self.math=math
        self.english=english
        self.japanese=japanese
        self.science=science
        self.society=society
    def average_score(self):
        ave=(self.math+self.english+self.japanese+self.science+self.society)/5
        return ave

student1=Student("斎藤そうま",82,74,60,92,72)
print(student1.average_score())
        

#練習問題
#アパレルネット通販のアプリで商品クラスを作るケース
class Product:
    def __init__(self,iD,name,price,purchase_price):
        self.iD=iD
        self.name=name
        self.price=price
        self.purchase_price=purchase_price
    def calculate(self):
        return self.purchase_price/self.price

product1=Product("A0001","半袖クールTシャツ",5000,2250)
print(product1.calculate())
product1.price=6000
print(product1.calculate())

