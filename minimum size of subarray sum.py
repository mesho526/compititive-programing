class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        INF = n + 1
        windowSum, l, ans = 0, 0, INF
        for r in range(n):
            windowSum += nums[r]
            while windowSum >= target:
                ans = min(ans, r - l + 1)
                windowSum -= nums[l]
                l += 1
        return ans if ans != INF else 0
