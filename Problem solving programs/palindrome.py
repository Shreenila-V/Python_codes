#Finding palindrome for number

num = int(input("Enter a number:"))
temp = num
rev = 0
while(num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if(temp == rev):
    print("This value is a palindrome number")
else:
    print("This value is not a palindrome number")

#Finding palindrome for string
string=input(("Enter a letter:"))
if(string==string[::-1]):
      print("The letter is a palindrome")
else:
      print("The letter is not a palindrome")
