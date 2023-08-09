#type
x="python"
print(type(x))

#index
x="python"
print(x[0])

#negative index
x="python"
print(x[-2])

#slicing
x="python"
print(x[1:3])

#negative slicing
x="python"
print(x[-4:-1])

#to print multiple line
wishes=""" all the best"""
print(wishes)

#compare the strings
wishes="""all the best"""
wishes1="""do your best"""
wishes2="""all the best"""
print(wishes == wishes1)
print(wishes == wishes2)

#join two strings
firstname="shree"
secondname="nila"
fullname=(firstname+secondname)
print(fullname)

#loop
name="nila"
for letter in name:
    print(letter)

#len
name="python"
print(len(name))

#lowercase
name="PYTHON"
print(name.lower())

#uppercase
name="python"
print(name.upper())

#partition
name="python"
print(name.partition('python'))

#isnumeric
name="1234"
print(name.isnumeric())

#find
information="""I am a student"""
print(information.find("am"))

#startswith
information="""I am a student"""
print(information.startswith("I"))
