class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if int(num) < 10 and k==0:
            return num
        nums = [n for n in num]
        stack = []
        stack.append(nums[0])
        for i in range(1, len(nums)):
            if stack:
                if int(nums[i]) < int(stack[len(stack)-1]) and k > 0:
                    stack.pop()
                    k-= 1
            if int(nums[i]) != 0:
                stack.append(nums[i])
            elif stack:
                stack.append(nums[i])
        if k > 0 and stack:
            for i in range(len(stack)-1, -1, -1):
                if k <= 0:
                    break
                elif (int(stack[i]) != 0):
                    stack.pop(i)
                    k-= 1
        if  not stack:
            return "0"
        return "".join(stack)


s = Solution()
print(s.removeKdigits("9", 1))


