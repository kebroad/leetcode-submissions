from collections import Counter 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s is None:
            return s
        letters = Counter(s)
        print(letters)
        result = -1
        for index, char in enumerate(s):
            if letters[char] == 1:
                return index
        return -1
s = Solution()

print(s.firstUniqChar("yytooo"))
