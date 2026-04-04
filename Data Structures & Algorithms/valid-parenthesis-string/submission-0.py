class Solution:
    def checkValidString(self, s: str) -> bool:
        leftminimum, leftmaximum = 0, 0

        for c in s:
            if c == "(":
                leftminimum, leftmaximum = leftminimum + 1, leftmaximum + 1
            elif c == ")":
                leftminimum, leftmaximum = leftminimum - 1, leftmaximum - 1
            else :
                leftminimum, leftmaximum = leftminimum - 1, leftmaximum + 1
            if leftmaximum < 0:
                return False
            if leftminimum < 0:
                leftminimum = 0
        return leftminimum == 0