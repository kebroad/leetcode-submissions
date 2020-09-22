class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_num = 0
        max_string = ''
        n = len(s)
        for mid in range(0,n):
            x = 0
            while (mid-x >= 0) and (mid +x <= n-1):
                if s[mid-x] != s[mid+x]:
                    break
                l = 2 * x + 1
                if l > max_num:
                    max_num = l
                    max_string = s[mid-x:mid+x+1] 
                x += 1
        for mid in range(0,n-1):
            x = 1
            while (mid - x + 1 >= 0 and mid + x < n):
                if s[mid-x+1] != s[mid+x]:
                    break
                l = 2 * x 
                if l > max_num:
                    max_num = l
                    max_string = s[mid-x+1:mid+x+1] 
                x += 1
        return max_string

s = Solution()
print(s.longestPalindrome("cbbd"))