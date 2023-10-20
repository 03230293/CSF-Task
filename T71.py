def find_common_elements(list1, list2):
  # Create an empty list to store the common elements
  common = []
  # Loop through the first list
  for element in list1:
    # Check if the element is also in the second list
    if element in list2:
      # Add the element to the common list
      common.append(element)
  # Return the common list
  return common

# Example
print(find_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))  # Should print [3, 4, 5]