## Module 7 Project T2 Shaft,Zachary 
from math import log2
import random

def myFunction(x):
    if x == 0:
        return 0
    elif (log2(x) * 7 % 17) < (x % 13):
        return (x + log2(x)) ** 3
    elif (log2(x) * 5 % 23) < (x % 19):
        return (log2(x) + 2) ** 3
    else:
        return (log2(x) ** 2) - x

def hillClimb(arr, start_index):
    if not arr or start_index < 0 or start_index >= len(arr):
        return None, None

    array_size = len(arr)
    current_index = start_index

    while True:
        left_index, right_index = current_index - 1, current_index + 1
        left_value = arr[left_index] if 0 <= left_index < array_size else float('-inf')
        right_value = arr[right_index] if 0 <= right_index < array_size else float('-inf')

        # Check for peak
        if arr[current_index] >= left_value and arr[current_index] >= right_value:
            return current_index, arr[current_index]

        # Update based on pit or shoulder
        if left_value is None and right_value is None:
            return current_index, arr[current_index]
        elif left_value is None and right_value > arr[current_index]:
            current_index = right_index
        elif right_value is None and left_value > arr[current_index]:
            current_index = left_index
        elif left_value == right_value:
            # Equal increases, search to the right
            current_index = right_index
        elif left_value > right_value:
            # Search the higher path
            current_index = left_index
        else:
            # Move towards any equal or higher neighbor (climbs if plateau)
            if left_value <= arr[current_index] <= right_value:
                current_index = right_index
            else:
                # No progress on shoulder - plateau or local maximum
                return current_index, arr[current_index]

# Test the hillClimb function with random start indices
array_size = 10000
function_array = [myFunction(x) for x in range(array_size)]

# Generate a random starting index
start_index = random.randint(1, array_size - 2)

# Apply hillClimb algorithm
peak_index, peak_value = hillClimb(function_array, start_index)

# Print the result
print(f"Local maximum index: {peak_index}, Value: {peak_value}")

result_index, result_value = hillClimb([6, 5, 5, 5, 4, 3, 2], 5)
print(f"Local maximum index: {result_index}, Value: {result_value}")

result_index, result_value = hillClimb([2, 5, 5, 5, 4, 3, 2], 5)
print(f"Local maximum index: {result_index}, Value: {result_value}")
