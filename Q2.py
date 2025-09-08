# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. 
# Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # Position to place the next non-zero element
    pos = 0  
    
    # First pass: move non-zero elements forward
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1
    
    # Second pass: fill remaining positions with 0
    for i in range(pos, len(nums)):
        nums[i] = 0


# Example usage
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
