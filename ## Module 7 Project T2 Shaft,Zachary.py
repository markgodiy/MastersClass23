def hillClimb(arr, start_index):
    if not arr or start_index < 0 or start_index >= len(arr):
        return None, None

    current_index = start_index

    while True:
        current_value = arr[current_index]

        left_index = current_index - 1 if current_index > 0 else None
        right_index = current_index + 1 if current_index < len(arr) - 1 else None

        left_value = arr[left_index] if left_index is not None else float('-inf')
        right_value = arr[right_index] if right_index is not None else float('-inf')

        print(f"Current Index: {current_index}, Current Value: {current_value}")
        print(f"Left Index: {left_index}, Left Value: {left_value}")
        print(f"Right Index: {right_index}, Right Value: {right_value}")

        # Check for peak: Three consecutive numbers are equal
        if (left_value == current_value) and (current_value == right_value):
            print("Found local maximum.")
            return current_index, current_value

        # Move towards the higher neighbor
        if right_value > left_value:
            print("Moving right.")
            current_index = right_index
        else:
            print("Moving left.")
            current_index = left_index

# Example usage:
my_array = [6, 5, 5, 5, 4, 3, 2]
result_index, result_value = hillClimb(my_array, 5)
print(f"Local maximum index: {result_index}, Value: {result_value}")


# python.exe .\hillclimb.py
# Current Index: 5, Current Value: 3
# Left Index: 4, Left Value: 4
# Right Index: 6, Right Value: 2
# Moving left.
# Current Index: 4, Current Value: 4
# Left Index: 3, Left Value: 5
# Right Index: 5, Right Value: 3
# Moving left.
# Current Index: 3, Current Value: 5
# Left Index: 2, Left Value: 5
# Right Index: 4, Right Value: 4
# Moving left.
# Current Index: 2, Current Value: 5
# Left Index: 1, Left Value: 5
# Right Index: 3, Right Value: 5
# Found local maximum.
# Local maximum index: 2, Value: 5
