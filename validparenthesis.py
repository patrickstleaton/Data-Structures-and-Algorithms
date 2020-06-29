#O(N) Time, O(N) Space
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for bracket in s:
            if bracket in dict.values():
                stack.append(bracket)
            elif bracket in dict.keys():
                if stack == []:
                    return False
                elif dict[bracket] != stack.pop():
                    return False
            else:
                return False
        return stack == []
