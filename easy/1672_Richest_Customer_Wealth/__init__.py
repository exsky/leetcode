class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for man_accounts in accounts:
            sum = 0
            for acc in man_accounts:
                sum += acc
            if sum > max: max = sum
            del sum
        return max
