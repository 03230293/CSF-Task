def multiply_lists(list1, list2):
  # create an empty list to store the result
  result = []
  # loop through the elements of both lists using zip function
  for x, y in zip(list1, list2):
    # multiply the corresponding elements and append to the result list
    result.append(x * y)
  # return the result list
  return result

list1 = [1, 2, 3]
list2 =[4, 5, 6]
print(multiply_lists(list1, list2)) # should print [4, 10, 18]