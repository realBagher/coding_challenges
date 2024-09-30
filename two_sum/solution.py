from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Args:
            nums (List[int]): A list of integers where you need to find two numbers that sum up to target.
            target (int): The target sum that you need to achieve by adding two numbers from nums.
        Returns:
            List[int]: A list of two integers representing the indices

        Raises:
            ValueError

        """
        num_to_index = {}

        for i, num in enumerate(nums):

            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
