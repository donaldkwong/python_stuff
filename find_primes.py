#num1 is the original number, num2 is the prime number, num3 is all of the primes,
num1 = int(input("Enter any positive integer: "))
num2 = num1 + 1
num3 = []
count = 0

def find_prime(a):
  '''find_prime(a) -> yes or no
  Prints whether a is a prime'''
  import math
  limit = int((math.sqrt(a)) + 1)
  for i in range(2, limit):
    value1 = a / i
    value2 = int(a / i)
    if value1 == value2:
      return "no"
  return "yes"

while count != 5:
  result = find_prime(num2)
  if result == "yes":
    num3.append(num2)
    count = count + 1
    num2 = int(num2 + 1)
  if result == "no":
    num2 = int(num2 + 1)

print(str(num3) + " are the first five primes after " + str(num1) + ". ")

