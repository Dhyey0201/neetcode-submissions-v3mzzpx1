class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        output = strs[0]
        iter = 1
        while iter < len(strs):
            currentString = strs[iter]
            loop = min(len(output), len(currentString))
            i = 0 
            while i < loop and currentString[i] == output[i]:
                i +=1
            output = output[:i]
            iter+=1
        return output