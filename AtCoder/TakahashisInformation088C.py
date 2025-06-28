# -*- coding: utf-8 -*-
C=[]
for _ in range(0,3):
    row=list(map(int,input().split()))
    C.append(row)
    
diff1=[]
diff2=[]
diff3=[]
diff4=[]
for i in range(0,3):
    diff1.append(C[i][0]-C[i][1])
    diff2.append(C[i][1]-C[i][2])
    diff3.append(C[0][i]-C[1][i])
    diff4.append(C[1][i]-C[2][i])
ok=False
if diff1[0] == diff1[1] == diff1[2]:
    if diff2[0] == diff2[1] == diff2[2]:
        if diff3[0] == diff3[1] == diff3[2]:
            if diff4[0] == diff4[1] == diff4[2]:
                ok=True
if ok:
    print("Yes")
else:
    print("No")    