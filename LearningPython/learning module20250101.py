# -*- coding: utf-8 -*-
#learning module
#モジュールとはpythonのプログラムが書かれているファイルでそれ単体で動かすのではなく別のファイルから利用されることを想定したファイル
#よって主な中身は関数の定義やクラスの定義がメインとなる
#利点はソースコードが膨大になることを防ぐ。部品化のイメージ。
#あらかじめ用意されているモジュールを標準ライブラリと呼ぶ。

#from インポートするファイル　import インポートする関数やクラス名
from my_module1 import Student
student1=Student("斎藤壮馬",82,74,60,92,77)
ave=student1.average_score()
print(ave)