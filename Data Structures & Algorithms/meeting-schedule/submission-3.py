"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)

        prevEnd = 0

        for i in range(len(intervals)):
            start = intervals[i].start

            if start < prevEnd:
                return False
            
            prevEnd = intervals[i].end
        
        return True