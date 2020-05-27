class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        copied = nums.copy()
        copied.sort()
        ans = []
        for curr in nums:
            ans.append(copied.index(curr))
        return ans
