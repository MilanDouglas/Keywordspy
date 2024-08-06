
from main import main

e1 = ouremployees("Bob", "Sales", "Director od Sales", 100000, 20)
e2 = ouremployees("Linda", "Executive", "CIO", 150000, 16)

print(e1.name)
print(e2.role)
print(e1.eligible_for_retirement())
