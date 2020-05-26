class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if not S and not T:
            return True
        stack1 = []
        for char in S:
            if char != '#':
                stack1.append(char)
            elif stack1:
                stack1.pop()
                
        stack2 = []
        for char in T:
            if char != '#':
                stack2.append(char)
            elif stack2:
                stack2.pop()
        return stack1 == stack2

foo = Solution()
foo.backspaceCompare("y#fo##f", "y#f#o##f")