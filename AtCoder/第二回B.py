# -*- coding: utf-8 -*-
S=input()
cnta=S.count("a")
cntb=S.count("b")
cntc=S.count("c")
mx=max(cnta,cntb,cntc)
if cnta==mx:
    print("a")
elif cntb==mx:
    print("b")
elif cntc==mx:
    print("c")
