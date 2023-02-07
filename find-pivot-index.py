class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        left_sum = 0

        for idx in range(len(nums)):
            right_sum = total_sum - left_sum - nums[idx]
            if left_sum == right_sum:
                return idx
            left_sum += nums[idx]

        return -1
