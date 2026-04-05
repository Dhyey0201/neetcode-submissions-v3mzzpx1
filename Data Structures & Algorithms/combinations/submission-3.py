class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start,combo):
            if len(combo) == k :
                result.append(combo.copy()) # We are saving copy because we don't need to change or add the changed value
                return
            
            #We are making decision tree here
            for i in range(start, n+1): # From Start till n(Including n)
                combo.append(i)
                backtrack(i+1,combo) # Recursion by incrementing i and with current combinations
                combo.pop()
        backtrack(1,[])
        return result