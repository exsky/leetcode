class Solution(object):
    def __init__(self):
        morse_mapping = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        morse_mapping.reverse()

        # 使用字典存 字母編號 對應的 摩斯密碼
        self.morse_dict = {}
        for i in self.char_range('a', 'z'):
            self.morse_dict[i] = morse_mapping.pop()

        # 存已轉換成摩斯的字串
        self.transed_morse_dict = {}

    def char_range(self, c1, c2):
        for c in range(ord(c1), ord(c2)+1):
            yield chr(c)

    def uniqueMorseRepresentations(self, words):
        # 所有串列中的字串轉 換成 摩斯密碼
        for word in words:
            w2m = ''
            for ch in word:
                w2m += self.morse_dict[ch]
            if w2m in self.transed_morse_dict:
                self.transed_morse_dict[w2m] += 1
            else:
                self.transed_morse_dict[w2m] = 1
        return len(self.transed_morse_dict)
