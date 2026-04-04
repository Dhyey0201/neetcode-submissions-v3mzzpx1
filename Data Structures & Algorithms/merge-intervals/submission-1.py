class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # First we will sort the interval
        # (key = lambda i : i[0]) ==> Its an inbuilt python func used to sort the intervals with any key like here it sorts with value of i and i[0] means the starting value of interval
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        # We will take out the start as well as first interval 2(here 1 as value starts form 0,1,2...)

        for start, end in intervals[1:]:
            lastend = output[-1][1] # This will take the max value of previous interval or the the value from which the previous interval is finished

            if start <= lastend:
                output[-1][1] = max(lastend, end)
            
            else:
                output.append([start,end])
        return output