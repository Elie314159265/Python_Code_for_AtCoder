# -*- coding: utf-8 -*-
import os
from datetime import datetime


def write_to_file():
    try:
        filename=input("ファイル名を入力してください:")
        print("内容を入力してください(空行で終了) :")
        lines=[]
        while True:
            line=input()
            if line == "":
                break
            lines.append(line + "\n")
            
        now=datetime.now()
        timestamp=now.strftime("%Y-%m-%d %H:%M:%S")
        lines.insert(0,f"[記録時刻]:{timestamp}")
        with open(filename,"a",encoding="utf-8") as f:
            #f.writelines(lines)
            f.write("\n".join(lines))
        print("ファイルを保存しました。")
    except Exception as e:
        print(f"保存中にエラーが発生しました。{e}")

def read_file():
    filename=input("ファイル名を入力してください:")
    try:
        with open(filename,"r",encoding="utf-8") as file:
            content=file.read()
            print("\n---メモ内容---")
            print(content)
    except FileNotFoundError:
        print("ファイル名が見つかりません")
    except UnicodeDecodeError:
        print("文字コードがあっていません。utf-8ではないかもしれません")
    except Exception as error:
        print(f"読み込み中にエラーが発生しました。{error}")
        
def delete_file():
    try:
        filename=input("削除するファイル名を入力してください:")
        if os.path.exists(filename):#カレントディレクトリのファイルのみ対象
            os.remove(filename)
            print(f"{filename}を削除しました。")
        else:
            print("指定されたファイルは存在しません")
    except Exception as e:
        print(f"削除中にエラーが発生しました。:{e}")

def main():
    while True:
        
        print("\n操作を選んでください")
        print("1: ファイルに書く")
        print("2: ファイルを読む")
        print("3. ファイルを削除")
        print("4: 終了")
        choice = int(input("選択(1-4):"))
        if choice==1:
            write_to_file()
        elif choice==2:
            read_file()
        elif choice==3:
            delete_file()
        elif choice==4:
            print("終了します\n")
            break
        else:
            print("正しい選択肢を入力してください")

    


if __name__ == "__main__":
    main()