class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        if n == 0:
            return ""
        m_string = s[0]
        m = 1
        for mid in range(n):
            offset = 1
            while (mid-offset >= 0) and (mid + offset < n) and (s[mid-offset] == s[mid+offset]):
                offset += 1
            m_test = (2*(offset-1)+1)
            offset -= 1
            if m_test > m:
                m = m_test
                m_string = s[mid-offset:mid+offset+1]

        for mid in range(n):
            offset = 1
            while (mid-offset+1 >= 0) and (mid + offset < n) and (s[mid-offset+1] == s[mid+offset]):
                offset += 1
            m_test = 2*(offset-1)
            offset -= 1
            if m_test > m:
                m = m_test
                m_string = s[mid-offset+1:mid+offset+1]                       
        return m_string
        # max_num = 0
        # max_string = ''
        # n = len(s)
        # for mid in range(0,n):
        #     x = 0
        #     while (mid-x >= 0) and (mid +x <= n-1):
        #         if s[mid-x] != s[mid+x]:
        #             break
        #         l = 2 * x + 1
        #         if l > max_num:
        #             max_num = l
        #             max_string = s[mid-x:mid+x+1] 
        #         x += 1
        # for mid in range(0,n-1):
        #     x = 1
        #     while (mid - x + 1 >= 0 and mid + x < n):
        #         if s[mid-x+1] != s[mid+x]:
        #             break
        #         l = 2 * x 
        #         if l > max_num:
        #             max_num = l
        #             max_string = s[mid-x+1:mid+x+1] 
        #         x += 1
        # return max_string

s = Solution()
print(s.longestPalindrome("cbbd"))