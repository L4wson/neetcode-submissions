class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        keys = {")": "(", "]": '[', "}": "{"}

        for char in s:
            if char in keys:
                if not stack or stack.pop() != keys[char]:
                    return False
            else:
                stack.append(char)
        return not stack
            