# -*- coding: utf-8 -*-

class BankAccount:
    
    def __init__(self,owner):
        self.__owner=owner
        self.__balance=0
        self.__history=[] #Log
    
    def deposit(self,amount):
        if amount <= 0:
            print("Invalid amount")
            self.__history.append("[Deposit] Failed: Invalid amount")
        else :
            self.__balance += amount
            self.__history.append(f"[Deposit] + {amount} -> Balance: {self.__balance}")
    
    def withdraw(self,amount):
        if self.__balance < amount:
            print("your balance is not sufficient")
            self.__history.append("[Withdraw] Filed: Insufficient funds")
        else :
            self.__balance= self.__balance - amount
            self.__history.append(f"[Withdraw] - {amount} -> Balance: {self.__balance}")
    def get_balance(self):
        return self.__balance
    
    def get_owner(self):
        return self.__owner
    
    def show_history(self):
        for history in self.__history:
            print(history)
    
class Bank:
    def __init__(self):
        self.__accounts={} #name -> BankAccount
        self.__passwords = {} #name -> Password
        self.__login_id_user=None
        
    def create_account(self,name,password):
        if name in self.__accounts:
            print(f"Account for {name} already exist")
        else :
            self.__accounts[name]=BankAccount(name)
            self.__passwords[name]=password
            print(f"Account created for {name}")
    
    def login(self,name,password):
        if name in self.__accounts and self.__passwords[name] == password:
            self.__login_id_user=name
            print(f"{name} logged in successfully")
    def logout(self):
        if self.__login_id_user:
            print(f"{self.__login_id_user} logged out.")
            self.__login_id_user=None
        else :
            print("No user is currently logged in")
    
    
    def deposit(self,amount):
        if self.__login_id_user:
            self.__accounts[self.__login_id_user].deposit(amount)
        else:
            print("Please log in first")
    
    def withdraw(self,amount):
        if self.__login_id_user:
            self.__accounts[self.__login_id_user].withdraw(amount)
        else:
            print("Please Log in first")
            
    def show_balance(self):
        if self.__login_id_user:
            balance = self.__accounts[self.__login_id_user].get_balance()
            print(f"Balance for {self.__login_id_user}: {balance}")
        else:
            print("Please log in first.")
        
    def show_history(self):
        if self.__login_id_user:
            self.__accounts[self.__login_id_user].show_history()
        else:
            print("Please log in first.")



bank = Bank()

# アカウント作成
bank.create_account("Alice", "password123")
bank.create_account("Bob", "bobpass")

# ログイン
bank.login("Alice", "password123")
bank.deposit(1000)
bank.withdraw(300)
bank.show_balance()
bank.show_history()
bank.logout()

# 別のユーザーでログイン
bank.login("Bob", "wrongpass")    # 失敗
bank.login("Bob", "bobpass")      # 成功
bank.deposit(500)
bank.show_balance()