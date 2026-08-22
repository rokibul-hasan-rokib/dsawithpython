numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10
           ]
target = 5

for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Element found at index {i}")
        break