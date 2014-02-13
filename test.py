#  File:       test.py

def factorial(n): 
  if n == 0: 
    return 1 
  else: 
    return n * factorial(n-1) 

print (" 5! has a value of: ",)
result = factorial(5)
print (result)

print (" 4! has a value of:",)
result = factorial(4)
print (result)

