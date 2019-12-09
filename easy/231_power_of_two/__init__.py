class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num_bin = "{0:b}".format(n)
        len_bin = len(num_bin)

        if len_bin == 1 and num_bin[0] == '0':
            return False

        for i in range(1, len_bin):
            if num_bin[i] == '1':
                return False
        return True
