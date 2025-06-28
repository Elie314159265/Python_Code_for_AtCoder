# -*- coding: utf-8 -*-
N=int(input())

if N%2 == 1:
    print("Odd")
else :
    print("Even")
    


S=input()
count=[0]*26
for ch in S:
    index=ord(ch)-ord('a')
    count[index]+=1

for i in range(26):
    print(f"{chr(ord('a')+i)}:{count[i]}")