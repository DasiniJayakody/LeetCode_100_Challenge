# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    # Initialize the result array with 1s
    answer = [1] * n

    # Calculate prefix products
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Calculate postfix products and multiply with prefix
    postfix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]

    return answer

# Example usage
nums = [1, 2, 3, 4]
result = product_except_self(nums)
print("Input:", nums)
print("Output:", result)

