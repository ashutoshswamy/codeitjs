def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1 

arr = [10, 24, 35, 42, 53, 61, 78]
target = 42

result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
