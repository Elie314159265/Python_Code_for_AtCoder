# -*- coding: utf-8 -*-
"""　2025/04/23　ファイル操作復習 
from datetime import datetime
import os 
def filedelete():
    filename=input("削除するファイル名を入力してください:")
    if os.path.exists(filename):
        os.remove(filename)
        print("ファイル名が削除されました。")
    else :
        print("指定されたファイルは存在しませんｎ")

def filewrite(): 
    filename=input("ファイル名を入力してください:")
    print("ファイルの内容を書いて下さい(空行で終了)")
    lines=[]
    while True:
        line=input()
        if line=="":
            break
        else:
            lines.append(line)
        
    now=datetime.now()
    timestamp=now.strftime("%Y-%m-%d %H:%M:%S")
    lines.insert(0,f"記録時刻:{timestamp}")
    with open(filename,"a",encoding="utf-8") as file:
        file.write("\n".join(lines))
    print("ファイルを保存しました。")

def fileread():
    filename=input("ファイル名を入力してください:")
    with open(filename,"r",encoding="utf-8") as file:
        content=file.read()
        print(content)
    
print("メニューを選択してください　1:read  2:write 3:delete")
choice=int(input())
if choice==1:
    fileread()
elif choice==2:
    filewrite()
elif choice==3:
    filedelete()
else :
    print("Invalid option")
    """