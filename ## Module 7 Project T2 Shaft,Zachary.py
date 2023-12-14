def hillClimb(arr, start_index):
    if not arr or start_index < 0 or start_index >= len(arr) - 1:
        return None, None

    current_index = start_index

    while True:
        current_value = arr[current_index]

        left_index = current_index - 1
        right_index = current_index + 1

        left_value = arr[left_index] if left_index >= 0 else float('-inf')
        right_value = arr[right_index] if right_index < len(arr) else float('-inf')

        # Print current state for debugging
        print(f"L({left_value}) [{current_index}]={current_value} R({right_value})")

        # Check if the current value is greater than or equal to its neighbors
        if current_value >= left_value and current_value >= right_value:
            # check two neighbors to see if they are greater
            if current_index + 2 < len(arr) and arr[current_index + 2] > arr[current_index + 1]:
                current_index += 2
                continue
            # check two neighbors to see if they are less
            elif current_index - 2 >= 0 and arr[current_index - 2] > arr[current_index - 1]:
                current_index -= 2
                continue
            else: 
                print("Found local maximum.")
                return current_index, current_value

        # Move right if right_value is greater, or left if not
        current_index = right_index if right_value > left_value else left_index

# Example usage:
my_array = [6, 5, 5, 5, 4, 3, 2]
result_index, result_value = hillClimb(my_array, 5)
print(f"Local maximum index: {result_index}, Value: {result_value}")
