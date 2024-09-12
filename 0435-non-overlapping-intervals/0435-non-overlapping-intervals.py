class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        ost = intervals[0][0]
        oet = intervals[0][1]
        count = 1
        for i in range(len(intervals)):
            nst = intervals[i][0]
            net = intervals[i][1]
            
            if oet <= nst:
                count += 1
                ost = nst
                oet = net
        
        return len(intervals) - count
            