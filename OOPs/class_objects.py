class student :
   def __init__(self,name,age):
      self.name=name
      self.age=age
   def display(self):
      print("name is:",self.name)
      print("age is:",self.age)
p1=student("shree",20)
p2=student("nila",20)
p1.display()
p2.display()

#supermarket
class Supermarket :
   def __init__(self,fruits,vegetables,icecreams,grocery):
      self.fruits=fruits
      self.vegetables=vegetables
      self.icecreams=icecreams
      self.grocery=grocery
   def buy(self):
      print("the price of 1 kg apple",self.fruits)
      print("the price of 1 kg potato",self.vegetables)
      print("the price of 2 ice balls",self.icecreams)
      print("the price of wheat,biscuits,egg",self.grocery)
a=Supermarket(210,50,40,100)
a.buy()

#new code for destructor
class student :
   def __init__(self,name,age):
      self.name=name
      self.age=age
   def display(self):
      print("name is:",self.name)
      print("age is:",self.age)
   def __del__(self):
      print("name is not",self.name)
p1=student("shree",20)
p2=student("nila",20)
p1.display()
p2.display()





