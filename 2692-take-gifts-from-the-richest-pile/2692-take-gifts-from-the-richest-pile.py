import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gift = [-i for i in gifts]
        heapq.heapify(gift)
        for i in range(k):
            val = -heapq.heappop(gift)
            ele = math.floor(val**0.5)
            heapq.heappush(gift,-ele)
        return -(sum(gift))
