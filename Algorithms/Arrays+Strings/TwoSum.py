
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dict:
                return [i, dict[complement]]
            dict[num] = i


# Complexity Analysis

# Time complexity: O(n)O(n). We traverse the list containing nn elements only once. Each lookup in the table costs only O(1)O(1) time.

# Space complexity: O(n)O(n). The extra space required depends on the number of items stored in the hash table, which stores at most nn elements.

