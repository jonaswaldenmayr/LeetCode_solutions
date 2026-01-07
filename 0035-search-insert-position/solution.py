class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            idx = nums.index(target)
            print(idx)
            return idx
        else:
            for i,n in enumerate(nums):
                if target < nums[i]:
                    return i
            return len(nums)
