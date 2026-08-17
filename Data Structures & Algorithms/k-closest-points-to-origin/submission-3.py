class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]
        heap = []

        for x, y in points:
            d = -(x*x + y*y)
            if len(heap) < k:
                heapq.heappush(heap, (d, x, y))
            
            elif d > heap[0][0]:
                heapq.heapreplace(heap, (d, x, y))

        return [[x, y] for _, x, y in heap]