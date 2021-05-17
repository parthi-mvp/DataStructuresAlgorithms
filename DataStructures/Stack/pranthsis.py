class Solution:
    def isValid(self, A):
        if len(A) % 2 != 0:
            return 0
        stack = []
        close_paren = set([('(', ')'), ('[', ']'), ('{', '}')])
        for i in A:
            if i == '{' or i == '(' or i == '[':
                stack.append(i)
            elif i == '}' or i == ')' or i == ']':
                if len(stack) == 0:
                    return 0
                last = stack.pop()
                if (last, i) not in close_paren:
                    return 0

        return int(len(stack) == 0)


cl = Solution().isValid('({)')
print(cl)