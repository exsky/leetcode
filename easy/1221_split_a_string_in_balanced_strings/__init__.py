class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_Bal = 0
        count_L = 0
        count_R = 0
        for c in s:
            if c == 'L':
                count_L += 1
            if c == 'R':
                count_R += 1
            if count_L == count_R:
                count_Bal += 1
        return count_Bal
