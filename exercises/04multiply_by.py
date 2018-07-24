# Write a method called `multiply_by` that takes a number and
# array, and returns the array of numbers multiplied by that number.
#
# You'll want to apply your fundamental programming knowledge here.
# What are the pieces to this problem? You'll need to define a method,
# need a return statement, need a for loop to iterate over the array.
#
# Example method call:
#
# multiply_by([1, 2, 3], 5)
#
# > [5, 10, 15]

def multiply_by(lst, num):
  ret_list = []
  for i in lst:
    ret_list.append(i*num)
  return ret_list

arr = [1,2,3]

print(multiply_by(arr, 5))