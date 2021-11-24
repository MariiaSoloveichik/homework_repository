"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Function finds a sub-array with length less equal to k, with max sum
    nums - List to process, k - Max length of sub-array
    return - Max sum of sub-array
    """
    if len(nums) == 0 or k == 0:
        return 0
    max_sum = max(nums)
    while k > 0:
        for i in range(len(nums) - k + 1):
            if sum(nums[i: i + k]) > max_sum:
                max_sum = sum(nums[i: i + k])
        k -= 1
    return max_sum
