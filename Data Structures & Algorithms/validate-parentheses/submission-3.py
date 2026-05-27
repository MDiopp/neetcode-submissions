class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
               stack.append(char)
               continue
            if stack:
                top = stack[-1]
            elif not stack:
                if char == ')' or char == '}' or char == ']':
                    return False
                continue
            if (char == ')'and top == '(') or (char == '}' and top == '{') or (char == ']' and top == '['):
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False
            