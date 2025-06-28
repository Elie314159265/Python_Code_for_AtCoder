# -*- coding: utf-8 -*-
listN=list(map(int,input().split()))
listN=sorted(listN)
listN=list(reversed(listN))
#listN=sorted(listN,reverse=True)でもよい

print(listN[2])