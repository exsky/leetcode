class Solution:
    def countTriples(self, n: int) -> int:
        c_squ = []
        for c in range(2, n+1):
            c_squ.append(c*c)
        ans = 0
        for i in range(1, n):
            for j in range(i+1, n):
                if i*i + j*j in c_squ:
                    ans += 1
        return ans*2
