# -*- coding: utf-8 -*-
#divide=["dream","dreamer","erase","eraser"]
#reversedDivide=["","","",""]
#for x in range(0,4):
#    reversedDivide[x]=''.join(list(reversed(divide[x])))

#S=input("英小文字(1~10^5):")
#S=''.join(list(reversed(S)))

#模範解答以下
#replace()でSの中にある４つの文字列を空文字列に置換する。
s = input().replace("eraser","").replace("erase","").replace("dreamer","").replace("dream","")

if s:
    print("NO")
else:
    print("YES")