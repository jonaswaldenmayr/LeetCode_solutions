class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n, m = 0, len(nums) -k
        heapq.heapify(nums)

        while n < m:
            heapq.heappop(nums)
            n += 1
        return nums[0]
