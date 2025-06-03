import heapq

class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        min_heap = []

        for left, right in intervals:
            if min_heap and left > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, right)
            else:
                heapq.heappush(min_heap, right)
        return len(min_heap)

sol = Solution()
