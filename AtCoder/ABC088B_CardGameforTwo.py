# -*- coding: utf-8 -*-
N=int(input("N(1~100):"))
ai=list(map(int,input("ai(1~100)").split()))
Alice=0
Bob=0
ai=sorted(ai,reverse=True)
for cnt in range(0,N,2):
    Alice+=ai[cnt]
    if cnt==N-1:
        break
    Bob+=ai[cnt+1]
subScore=Alice-Bob
print(f"subScore:{subScore}")
