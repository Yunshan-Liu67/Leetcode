class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        store = nums.copy()
        removed = 0
        i = 1
        while i < len(nums):
            if store.count(nums[i]) > 1:
                for j in range(1,store.count(nums[i])):
                    nums.remove(nums[i])
                    removed += 1
            else:
                pass   
            i += 1
        nums.sort()
        length = len(nums)
        return length
