class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    #    result = 0

     #   for i in range(len(s)):
      #      charset = set()
       #     for j in range(i, len(s)):
        #        if s[j] in charset:
         #           break
         #       charset.add(s[j])
         #   result = max(result, len(charset))
        #return result

        #optimal solution using sliding window 

        charset = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            result = max(result, r - l + 1)
        return result