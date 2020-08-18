from collections import Counter 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = Counter(s)
        t_cnt = Counter(t)
        for s_i in s_cnt:
            if t_cnt[s_i] != s_cnt[s_i]:
                return False
        for t_i in t_cnt:
            if t_cnt[t_i] != s_cnt[t_i]:
                return False
        return True

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
