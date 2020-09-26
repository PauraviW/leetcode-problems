class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals.sort()

        if len(intervals) <= 1:
            return intervals

        max_in = intervals[0][1]
        ran = intervals[0][1] - intervals[0][0]

        ans = []

        # for i, c in enumerate(intervals):
        #     if c[0] > max_in:
        #         ans.append([max_in - ran, max_in])
        #         max_in = c[1]
        #         ran = c[1] - c[0]
        #     else:
        #         if c[1] > max_in:
        #             ran = ran + (c[1] - max_in)
        #             max_in = c[1]
        #     if i == (len(intervals) - 1):  # we need to put this case here so we don't miss the last interval
        #         ans.append([max_in - ran, max_in])
        start = intervals[0][0]
        end = intervals[0][1]

        for i, x in enumerate(intervals):
            print(x)
            if x[0] > end and x[1] > end:
                ans.append([start, end])
                start = x[0]
                end = x[1]
            else:
                if x[1] > end and x[0]<=end:
                    end = x[1]
        ans.append([start, end])
        return ans

intervals = [[0,8],[1,2],[2,4],[10,15],[14,16]]
print(Solution().merge(intervals))