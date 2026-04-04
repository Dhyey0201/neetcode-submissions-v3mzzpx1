class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        newstr = []

        while i < len(word1) and j < len(word2):
            newstr.append(word1[i])                
            newstr.append(word2[j])
            i+=1
            j+=1
        newstr.append(word1[i:])                
        newstr.append(word2[j:])
        return "".join(newstr)