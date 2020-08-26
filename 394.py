import re
from typing import List
########## UNFINISHED #####################


# class Solution:
#     def decodeString(self, s: str) -> str:
#         isNum = re.compile("[0-9]")
#         finalstring = ''
#         index = 0
#         while index < len(s):
#             ###################################
#             if isNum.match(s[index]):
#                 amount = int(s[index])
#                 index += 2
#                 substring = ''
#                 while s[index] != ']':
#                     if isNum.match(s[index]):
#                         amount2 = int(s[index])
#                         index2 += 2
#                         substring2 = ''
#                         while s[index] != ']':
#                             if isNum.match(s[index]):
#                                 amount2 = int(s[index])
#                                 index2 += 2
#                                 substring2 = ''
#                                 while s[index] != ']':
#                             else:
#                                 substring += s[index]
#                     else:
#                         substring += s[index]
#                     index += 1
#                 for i in range(amount):
#                     finalstring += substring
#             ########################################
#             elif isChar.match(s[index]):
#                 finalstring += s[index]
#             index += 1
#         return finalstring
#     def processNumString(index, s: string):
#             index += 2
#             amount = int(s[index])
#             substring = ''
#             while s[index] != ']':
#                 if s[index] == 

class Solution:
    def decodeString(self, s: str) -> str:
        isNum = re.compile("[0-9]")
        final = ''
        index = 0
        s = []
        inBracket = False
        while index < len(s):
            if isNum.match(s[index]):
                count = 10*count + int(s[index])
                count = int(s[index])
            elif s[index] == '[':
                s.append({count, final})
            elif s[index] == ']':
                count, final = s.pop()
                final += count* final
                count = 0
            else:
                final += s[index] 
            count += 1
        return final
        


s = Solution()
print(s.decodeString("3[a2[c]]")
)
