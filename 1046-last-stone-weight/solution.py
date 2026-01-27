class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first < second: #first will be more negative than second!
                heapq.heappush(stones, first-second)

        stones.append(0)
        return abs(stones[0])
