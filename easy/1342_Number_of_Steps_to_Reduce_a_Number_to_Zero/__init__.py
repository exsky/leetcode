class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            # zero
            return 0
        elif num % 2 == 0:
            # even
            return 1 + self.numberOfSteps(num/2)
        else:
            # odd
            return 1 + self.numberOfSteps(num-1)
