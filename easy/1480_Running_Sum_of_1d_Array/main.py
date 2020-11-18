class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if not ans:
                ans.append(i)
            else:
                ans.append(ans[-1]+i)
        return ans
