#Mini Caclculator
x = float(input("Give me a number: "))
o = input("Give an operator: ")
y = float(input("Give me another number: "))

if o == "+":
  print(x + y)
elif o == "-":
    print(x - y)
elif o == "/":
  print(x / y)
elif o == "*":
  print(x * y)
elif o == "**" or o == "^":
  print(x ** y)
else:
  print("Unknown Operator.")