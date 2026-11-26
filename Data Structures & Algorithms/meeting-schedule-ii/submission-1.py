"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        40, 20
        '''

        if len(intervals) <= 1:
            return len(intervals)

        intervals.sort(key = lambda x: x.start)
        heap = []
        heapq.heappush(heap, intervals[0].end)
        rooms_req = 0

        for interval in intervals[1:]:
            start, end = interval.start, interval.end
            while heap and heap[0] <= start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
            rooms_req = max(rooms_req, len(heap))
        
        return rooms_req
            



