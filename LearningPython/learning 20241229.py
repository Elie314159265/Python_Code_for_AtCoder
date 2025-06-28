# -*- coding: utf-8 -*-
pi=3.14159
diameter=11.2 #直径
area=pi*(diameter/2)**2 #面積
print(area) #面積出力

x,y,z=3,221,311
answer = min(x,y,z)
if x%2 != 0:
    answer = x
if y%2 != 0 and y>answer:
    answer=y
if z%2 != 0 and z>answer:
    answer = z
#print(answer)
#name = input('Enter name : ')
#print('Are you really',name,'?' )

#birthday = input('Enter your birthday date mm/dd/yyyy:')
#print('you were born in the year',birthday[-4:])
i=0
max=-1000
#num_x=int(input("how many times should I print the letter X?"))
#to_print=''
#while(i<num_x):
#    to_print=to_print+'X'
#    i=i+1
#print(to_print)
while(i<10):
    x=int(input('write 10 numbers:'))
    if x>max and x%2!=0:
        max=x
    i=i+1
if max==-1000:
    print('No odd number')
else :
    print(max)

    