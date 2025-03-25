class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        def overlap(intervals):
            intervals.sort()

            section = 0
            max_end = intervals[0][1]
            for s,e in intervals:
                if max_end <= s:
                    section += 1
                max_end = max(max_end,e)
                if section >= 2:
                    return True
            return False

        x_interval = [[i[0], i[2]] for i in rectangles]
        y_interval = [[i[1], i[3]] for i in rectangles]

        return overlap(x_interval) or overlap(y_interval)