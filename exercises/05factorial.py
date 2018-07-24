# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example method call
#
# factorial(5)
#
# > 120
#
def factorial(num):
  fac_range = list(range(1,num))[::-1]
  product = num
  for i in fac_range:
    product *= i
  return product

print(factorial(5))

