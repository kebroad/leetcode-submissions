from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        m = [[0 for _ in range(n)] for _ in range(n) ]
        for dif in range(0,n):
            for i in range(0, n-dif):
                if s[i:i+dif+1] in wordDict:
                    m[i][i+dif] = 1
                else:
                    for j in range(i+1,i+dif+1):
                        if m[i][j-1] and m[j][i+dif]:
                            m[i][i+dif] = 1
        if m[0][n-1] == 1:
            return True
        else:
            return False

s = Solution()
print(s.wordBreak("Iamace", ["I" , "am" , "ace" , "a" ]))


