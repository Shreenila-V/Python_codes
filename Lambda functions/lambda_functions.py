greet = lambda : print('Hello World')
greet()

#name user
my_name=lambda name:print("Hi,I am",name)
my_name("nila")

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)

# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)

#map()
x_1=[1,2,3,4]
y_1=[5,6,7,8]
new_list=list(map(lambda x,y:x+y,x_1,y_1 ))
print(new_list)

# program to reduce item in a list
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print("Sum:", sum)

#if else in lambda functions
to_check=lambda x:True if(x>10 and x<20) else False
print(to_check(12))
print(to_check(21))






