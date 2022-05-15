# Find the biggest contiguous substring of a specified length
def maxsum(arr, k=1):
    # Using sliding window
    max = 0
    window_sum = 0
    start = 0

    for end in range(len(arr)):
        window_sum += arr[end]

        if end >= k-1:  # Only slide when window reaches full length
            max = window_sum if window_sum > max else max

            # Slide the window
            window_sum -= arr[start]   # Element will no longer be in window
            start += 1
    return max



ex1 = [2, 1, 5, 1, 3, 2]
ex2 = [2, 3, 4, 1, 5]

print(maxsum(ex1, k=3))
print(f"Expected Output: 9 from {ex1} with k=3")
print(maxsum(ex2, k=2))
print(f"Expected Output: 7 from {ex2} with k=2")