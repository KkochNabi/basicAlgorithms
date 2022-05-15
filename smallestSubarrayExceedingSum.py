# Find the smallest sized subarray whose sum is equal or greater to a specified target
def smallest_subarray_exceeding_sum(arr, target_sum):
    # Use sliding window with dynamic size
    window_start = 0
    current_sum = 0
    # Set to impossible value because we're trying to find the smallest value later
    smallest_len = len(arr)+1

    # Keep expanding window until target sum is reached
    for window_end in range(len(arr)):
        current_sum += arr[window_end]

        while current_sum >= target_sum:
            smallest_len = min(window_end - window_start + 1, smallest_len)  # +1 because 0-index arrays

            # Keep shrinking the window from the start until sum is smaller than target
            current_sum -= arr[window_start]
            window_start += 1

    return smallest_len if smallest_len != len(arr)+1 else 0


ex1, s1, o1 = [2, 1, 5, 2, 3, 2], 7, 2
ex2, s2, o2 = [2, 1, 5, 2, 8], 7, 1
ex3, s3, o3 = [3, 4, 1, 1, 6], 8, 3

ex = [ex1, ex2, ex3]
s = [s1, s2, s3]
o = [o1, o2, o3]

for i in range(3):
    print(f"Output: {smallest_subarray_exceeding_sum(ex[i], s[i])}\tExpected Output: {o[i]}\tTarget Sum: {s[i]}\tArray: {ex[i]}")
