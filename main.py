#BUDGET APP
#Shoes.py
#Define a class of shoes
class Shoes:
    def __init__(self, name, price):
          self.name = name
          self.price = float(price)

    def budget_check(self, budget):
          if not isinstance(budget, (int, float)):
            print("Invalid entry. Please enter a number.")
            exit()
    def change(self, budget):
          return (budget - self.price)

    def buy(self, budget):
          self.budget_check(budget)

          if budget >= self.price:
            print(f"You can get {self.name}")

          if budget == self.price:
            print("You have enough money")

          else:
            print(f"You can get the" +self.name+ "and have ${self.cange(budget) left over")
          exit("Thanks for using our shoe budget app!")  
      
            
#Shoepurchase.py
from  Shoes import Shoes
low = Shoes('And 1s', 30)
medium = Shoes('Air Force 1s', 120)
high = Shoes('Off Whites', 400)

try:
  shoe_budget = float(input('What is your shoe budget? '))
except ValueError:
  exit('Please enter a number')

for shoes in [high, medium, low]:
  shoes.buy(shoe_budget)