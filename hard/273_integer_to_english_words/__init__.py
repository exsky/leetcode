dict_d = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
}
dict_d2 = {
    2: 'Twenty',
    3: 'Thirty',
    4: 'Forty',
    5: 'Fifty',
    6: 'Sixty',
    7: 'Seventy',
    8: 'Eighty',
    9: 'Ninety'
}
dict_1x = {
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen'
}


class Solution(object):
    def trans_each_three_digit(self, digits):
        # int digits form 0 to 999
        out = []
        if digits > 99:
            d3 = int(digits/100)
            out += [dict_d[d3], 'Hundred']

        dxx = digits % 100
        if dxx > 19:
            d2 = int(dxx / 10)
            out += [dict_d2[d2]]
        if dxx > 9 and dxx < 20:
            out += [dict_1x[dxx]]
        else:
            d1 = dxx % 10
            if d1:
                out += [dict_d[d1]]
        return out

    def numberToWords(self, num):
        ans = []
        str_num = str(num)
        unit = {10: 'Billion', 7: 'Million', 4: 'Thousand'}

        len_num = len(str_num)
        #  10   : Billion
        # 9 ~ 7 : Million
        # 6 ~ 4 : Thousand

        if len_num == 10:
            ans = [dict_d[int(str_num[0])], unit[10]]
        if len_num > 6:
            n = int(str_num[:-6]) % 1000
            if n > 0:
                tmp = self.trans_each_three_digit(int(str_num[:-6]) % 1000)
                tmp.append(unit[7])
                ans += tmp
        if len_num > 3:
            n = int(str_num[:-3]) % 1000
            if n > 0:
                tmp = self.trans_each_three_digit(int(str_num[:-3]) % 1000)
                tmp.append(unit[4])
                ans += tmp
        if num > 0:
            ans += self.trans_each_three_digit(num % 1000)
            return ' '.join(ans)
        else:
            return 'Zero'
