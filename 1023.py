from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        l = []
        work_string = ''
        for char in pattern:
            if ord(char) <= 90:
                l.append(work_string)
                work_string = char
            else:
                work_string += char
        l.append(work_string)
        l.pop(0)
        matches = []
        for query in queries:
            match = True
            match_i = 0
            while query and match_i < len(l):
                pat = l[match_i]
                if query[0] == pat[0]:
                    pat = pat[1:]
                    query = query[1:]
                    while query and pat and ord(query[0]) > 90:
                        if query[0] == pat[0]:
                            pat = pat[1:]
                        query = query[1:]
                    while query and ord(query[0]) > 90:
                        query = query[1:]                        
                    if len(pat) > 0:
                        match = False
                        break
                else:
                    match = False
                    break
                match_i += 1
            if (len(query) != 0) or match_i != len(l):
                match = False
            matches.append(match)

        return matches
s = Solution()
print(s.camelMatch(["ControlPanel"], "CooP"))

print(ord("Z"))
print(ord("a"))