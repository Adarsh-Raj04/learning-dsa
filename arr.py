def max_area(height):

    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        curr_area = min(height[left], height[right]) * (right - left)
        max_area = max(curr_area, max_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


# =---------------- Sliding Windonw ----------------
def max_sum(arr, k):

    if k <= 0 or k > len(arr):
        return -1

    # First window
    window_sum = 0

    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum

    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]

        max_sum = max(max_sum, window_sum)

    return max_sum


# ------------------ minimum sub array sum of size k ----------------
def min_subarray_len(arr, target):
    left = 0
    window_sum = 0
    min_length = float("inf")

    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum >= target:
            current_length = right - left + 1
            min_length = min(min_length, current_length)

            window_sum -= arr[left]
            left += 1

    if min_length == float("inf"):
        return 0

    return min_length


# -------------- Prefix Sum ----------------
def prefix_sum(arr):
    prefix_sum_arr = [0] * len(arr)  # initialize a new array of the same length as arr
    prefix_sum_arr[0] = arr[
        0
    ]  # initialize the first element of prefix_sum_arr with the first element of arr

    for i in range(1, len(arr)):
        prefix_sum_arr[i] = (
            prefix_sum_arr[i - 1] + arr[i]
        )  # calculate the prefix sum for each element in arr and store it in prefix_sum_arr

    return prefix_sum_arr


# ------------------ Range Sum ----------------
def range_sum(prefix_sum_arr, left, right):
    if left == 0:
        return prefix_sum_arr[right]
    else:
        return prefix_sum_arr[right] - prefix_sum_arr[left - 1]


# ------------------ Subarray Sum Equals K ----------------
def subarray_sum(arr, k):
    prefix_count = {0: 1}

    current_sum = 0
    count = 0

    for num in arr:
        current_sum += num

        needed = current_sum - k

        if needed in prefix_count:
            count += prefix_count[needed]

        prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

    return count


# ------------ Longest Consecutive ----------------
def longest_consecutive(nums):
    nums_set = set(nums)
    longest = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            length = 1

            while num + length in nums_set:
                length += 1

            longest = max(longest, length)

    return longest


# ------------------ valid Anagram ----------------
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True


# ------------------ valid Parentheses ----------------
def is_valid_parentheses(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


# ------------------- next greater element ----------------
def next_greater(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            pi = stack.pop()
            result[pi] = nums[i]

        stack.append(i)
    return result


# ------------------- next smaller element ----------------
def next_smaller(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        while stack and nums[i] <= stack[-1]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(nums[i])
    return result
