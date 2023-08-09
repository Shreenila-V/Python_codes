#atm
class Atm :
   def __init__(self,pin,amount,receipt):
      self.pin=pin
      self.amount=amount
      self.receipt=receipt
   def withdraw(self):
      print("enter the pin:",self.pin)
      print("enter the amount:",self.amount)
      print("collect the receipt:",self.receipt)
b=Atm("xxxx",1000,"receipt collected")
b.withdraw()
