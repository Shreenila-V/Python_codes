def a(n):
    if n==0:
        return
    else:
        a(n-1)
        print(" * "*n)
n = 5
a(n)

#mulitiplication pattern
rows = 8
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        square = i * j
        print(i * j, end='  ')
    print()

#
x=1*1*1*1+6*6*6*6+3*3*3*3+4*4*4*4
print(x)
