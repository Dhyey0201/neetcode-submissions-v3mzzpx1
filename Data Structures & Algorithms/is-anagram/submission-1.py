class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        hshmp = defaultdict(int)

        for i in s:
            hshmp[i] += 1

        for i in t:
            hshmp[i] -= 1

        for i in hshmp:
            if hshmp[i] != 0:
                return False
        return True