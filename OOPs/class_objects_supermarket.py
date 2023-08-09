#supermarket
class Supermarket :
   def __init__(self,fruits,vegetables,icecreams,grocery,total_bill):
      self.fruits=fruits
      self.vegetables=vegetables
      self.icecreams=icecreams
      self.grocery=grocery
      self.total_bill=total_bill
   def buy(self):
      print("the price of 1 kg apple",self.fruits)
      print("the price of 1 kg potato",self.vegetables)
      print("the price of 2 ice balls",self.icecreams)
      print("the price of wheat,biscuits,egg",self.grocery)
      print("the total price is",self.total_bill)
   def __del__(self):
       print("cancel the bill for 1 kg apple",self.fruits)
       print("cancel the bill for 1 kg potato",self.vegetables)
       print("cancel the bill for 2 ice balls",self.icecreams)
       print("cancel the bill for wheat,biscuits,egg",self.grocery)
       print("the total price is",self.total_bill)
   def __del__(self):
       print("update the bill for 2 kg apple",self.fruits)
       print("update the bill for 2 kg potato",self.vegetables)
       print("update the bill for 1 ice ball",self.icecreams)
       print("update the bill for wheat and egg",self.grocery)
       print("the total price is",self.total_bill)
a=Supermarket(210,50,40,100,210+50+40+100)
a.buy()
a1=Supermarket(120,30,10,50,120+30+10+50)
a1.buy()
