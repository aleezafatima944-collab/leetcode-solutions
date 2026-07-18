class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i ,nums in enumerate(nums):
            if target-nums in seen:
                return[seen[target-nums],i]
            seen[nums]=i
        
        