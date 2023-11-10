def linear_search(numbers_list, target):
  for i in range(len(numbers_list)):
    if numbers_list[i] == target:
      return i

  return -1

my_list = [12, 24, 56, 34, 3]
my_target = 56
result = linear_search(my_list, my_target)

if result != -1:
  print(f"Element found at index {result} and position {result + 1}")
else:
  print("Element not found")
