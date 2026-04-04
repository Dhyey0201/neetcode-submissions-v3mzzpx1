class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        #Intution is we've to add and remove element so we will definately use stack

        stack = []

        for ops in operations:
            if ops == "D":
                stack.append(2*stack[-1])
            elif ops == "C":
                stack.pop()
            elif ops == "+":
                stack.append(stack[-1] + stack[-2])

            else:
                stack.append(int(ops))
        return sum(stack)
