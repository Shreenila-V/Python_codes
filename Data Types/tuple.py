#acees tuple(positive index)
x=(2,4,7,8,5)
print(x[3])
#acess tuple(negative index)
x=(2,4,7,8,5)
print(x[-3])
#type of tuple
x=(1,2,3,4,5)
print(type(x))
#slicing
x=(1,2,3,4,5)
print(x[0:3])
x=(1,2,3,4,5)
print(x[4:])
#index
x=(1,2,3,4,5)
index=x.index(2)
print(index)
#count
x=(1,2,3,4,5)
print(x.count(2))
#loop
x=(1,2,3,4,5)
for x in x:
    print(x)
#to check
x=(1,2,3,4,5)
print(1 in x)
#operation
x=5/2
print(x)
#operation
x=5.2/2
print(x)
#tuple to list
x=(1,2,3,4,5)
x=list(x)
print(dsx)
#list to tuple
x=[1,2,3,4,5]
x=tuple(x)
print(x)
#printing the tuple and assign to new tuple
x=(1,2,3,4,5)
print(x[:])
y=x[:]
print("y=",x)
#to check the value inside the tuple
x=(1,2,3,4,5)
print(2 in x)
#to check the value inside the tuple
x=(1,2,3,4,5)
print(6 in x)
#to check for a invalid index number
x=[1,2,3,4,5]
x[6]=2
print(x)
#the error when we give invalid index number says that assignment index out of range

