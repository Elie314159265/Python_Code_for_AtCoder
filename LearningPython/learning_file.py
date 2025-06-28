# -*- coding: utf-8 -*-
"""ファイルオープン
try:
    filename=input("ファイル名を入力してください：")
    with open(filename,"r",encoding="utf-8") as f:
        content=f.read()
        print(f"ファイルの内容{content}")
except FileNotFoundError:
    print("指定したファイル名が見つかりません")
except UnicodeDecodeError:
    print("ファイルの文字コードがあっていません。utf-8以外かもしれません")
except Exception as e:
    print(f"その他のエラーが発生しました。{e}")

"""

"""ファイル書き込み
try:
        
    filename=input("ファイル名を指定してください:")
    text=input("ファイルに書き込む内容を入力してください:")
    with open(filename,"w",encoding="utf-8") as f:
        f.write(text)    
    print("ファイルへの書き込みが完了しました。")
except Exception as error:
    print(f"エラーが発生しました。:{error}")
    
"""

"""ファイル複数行書き込み
try:
    filename=input("ファイル名を指定してください:")
    print("ファイルに書き込む内容を指定してください(終了するには空行を入力):")
    lines=[]
    while True:
        line=input()
        if line == "":
            break
        lines.append(line + "\n")
    with open(filename,"w",encoding="utf-8") as f:
        f.writelines(lines)
    print("ファイルの書き込みが完了しました")
except Exception as error:
    print(f"エラーが発生しました:{error}")
"""