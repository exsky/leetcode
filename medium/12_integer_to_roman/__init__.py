class Solution(object):
    def intToRoman(self, num):
        b1 = num % 10
        b2 = int(num / 10) % 10
        b3 = int(num / 100) % 10
        b4 = int(num / 1000) % 10
        out = ""
        out += 'M' * b4
        if b3:
            if b3 == 9:
                out += 'CM'
            elif b3 == 4:
                out += 'CD'
            elif b3 > 5:
                count = b3 - 5
                out += 'D' + 'C' * count
            elif b3 == 5:
                out += 'D'
            elif b3 < 5:
                out += 'C' * b3
        if b2:
            if b2 == 9:
                out += 'XC'
            elif b2 == 4:
                out += 'XL'
            elif b2 > 5:
                count = b2 - 5
                out += 'L' + 'X' * count
            elif b2 == 5:
                out += 'L'
            elif b2 < 5:
                out += 'X' * b2
        if b1:
            if b1 == 9:
                out += 'IX'
            elif b1 == 4:
                out += 'IV'
            elif b1 > 5:
                count = b1 - 5
                out += 'V' + 'I' * count
            elif b1 == 5:
                out += 'V'
            elif b1 < 5:
                out += 'I' * b1
        return out
