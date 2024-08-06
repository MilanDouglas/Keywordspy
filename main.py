#Classes and Objects
class Employees:
  def __init__(self, name, department, role, salary, years_employed):
      self.name = name
      self.department = department
      self.role = role
      self.salary = salary
      self.years_employed = years_employed

  def eligible_for_retirement(self):
    if self.years_employed >= 20:
      return True
    else:
      return False

#object and code to in another python file
from main import main

e1 = ouremployees("Bob", "Sales", "Director od Sales", 100000, 20)
e2 = ouremployees("Linda", "Executive", "CIO", 150000, 16)

print(e1.name)
print(e2.role)
print(e1.eligible_for_retirement())
