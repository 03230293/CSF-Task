numbers=([2,9,3,0,5])
z=0
# def find_max(numbers):
#     for i in numbers:
#         n=i
#         if i != z:
#             print(numbers[-1])
# find_max(numbers)

def find_max(numbers):
  # initialize the maximum value to the first element of the list
  max_value = numbers[0]
  # loop through the rest of the list
  for num in numbers[1:]:
    # compare each element with the current maximum value
    if num > max_value:
      # update the maximum value if a larger element is found
      max_value = num
  # return the maximum value
  return max_value
find_max(numbers)