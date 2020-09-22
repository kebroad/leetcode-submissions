class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        max = 0
        run_sum = 1
        prev_num = s[0]
        for c in s[1:]:
            if c == prev_num:
                run_sum += 1
            else:
                run_sum = 1
            if run_sum > max:
                max = run_sum
            prev_num = c
        return max

s = Solution()
print(s.maxPower("leetcode"))