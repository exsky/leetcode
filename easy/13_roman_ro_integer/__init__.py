class Solution(object):
    def __init__(self):
        self.di = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def romanToInt(self, s):
        sum = self.di[s[-1]]
        for i in range(len(s)-1):
            curr = self.di[s[i]]
            if self.di[s[i+1]] > curr:
                sum -= curr
            else:
                sum += curr
        return sum
