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

        intervals.sort(key = lambda x: x.start)

        heap = []
        rooms_req = 0

        for i in range(len(intervals)):
            while heap and heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, intervals[i].end)
            rooms_req = max(rooms_req, len(heap))
        
        return rooms_req
