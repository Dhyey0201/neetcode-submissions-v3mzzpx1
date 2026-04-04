class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = [] # To store the values

        for i in range(len(intervals)):

            # Checking the first edge case if the interval is overlapping before the starting of the first interval

            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:] # Gives out result including hte new interval from i onwards

            # We will check if the the interval is after the current interval

            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # If both the above conditions fail it means the intervals are overlapping 

            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
        res.append(newInterval)
        return res