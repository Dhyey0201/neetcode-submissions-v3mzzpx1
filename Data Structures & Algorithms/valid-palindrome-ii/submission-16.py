class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skipl = s[l+1:r+1] # It will start from l+1 means second char and goes till r+1(r+1 means it includes also r)
                skipr = s[l:r] # it means it will start from first char and goes till second last char...i,e we've removed or skipped last char
                return (skipl == skipl[::-1] or skipr == skipr[::-1])
            l+=1
            r -= 1

        return True