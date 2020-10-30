from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        a = [1]* n
        a_cnt = [1]* n
        for j in range(1,n):
            sub_m = 1
            sub_m_cnt = 1
            for i in range(0, j):
                if nums[i] < nums [j]:
                    if ((a[i]) + 1) > sub_m:
                        sub_m = (a[i] + 1)
                        sub_m_cnt = 1
                    elif sub_m == a[i] + 1:
                        sub_m_cnt += 1 
            a[j] = sub_m
            a_cnt[j] = sub_m_cnt
        m = max(a)
        m_cnt = 0
        for i in range(n):
            if a[i] == m:
                m_cnt += a_cnt[i]
        return m_cnt



s = Solution()
print(s.findNumberOfLIS([1,2,4,3,5,4,7,2]))