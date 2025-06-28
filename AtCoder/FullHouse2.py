# -*- coding: utf-8 -*-
#map(使いたい関数,対象リストなど)で使うことができる
x=list(map(int,input().split()))
x=sorted(x)
if x[0]==x[1] and x[1]!=x[2] and x[2]==x[3] and x[0]>0 and x[3]<14:
    print("Yes")
elif  x[0]==x[1] and x[1]==x[2] and x[2]!=x[3] and x[0]>0 and x[3]<14:
    print("Yes")
elif x[0]!=x[1] and x[1]==x[2] and x[2]==x[3] and x[0]>0 and x[3]<14:
    print("Yes")
else :
    print("No")