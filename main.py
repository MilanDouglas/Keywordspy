def f():
   return ['foo', 'bar', 'baz', 'qux']
  

x = f()
print(x)

x = f()[2]
print(x)

x = f()[::-1]
print(x)
