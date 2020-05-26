class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = dict()
        parentheses[')'] = '('
        parentheses[']'] = '['
        parentheses['}'] = '{'

        for char in s:
            if char in parentheses:
                if not stack or stack.pop() != parentheses[char]:
                    return False
            else:
                stack.append(char)
        return not stack