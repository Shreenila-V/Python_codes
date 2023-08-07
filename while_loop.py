#while else loop
x=1
y="welcome"
while(x<5):
    print(x)
    x=x+1
else:
    print(y)

#while loop(program1)
i =1
while i<=10:
    print(i)
    i=i+1

#while loop(program2)
i=1
n=6
while i<=20:
    print(n,"*",i,"=",n*i)
    i=i+1

#while loop (program3)
a=[1,2,3,4,5]
i=4
while i<len(a):
    a[0]=a[0]+100
    a[1]=a[1]+100
    a[2]=a[2]+100
    a[3]=a[3]+100
    a[4]=a[4]+100
    i=i+1
    print(a)
