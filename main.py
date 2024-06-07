try:
  year = int(10 / 0.2)
  print(f"The result is {year} for now")
except ZeroDivisionError:
  print("cannot divide by zero")