class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range (len(nums)):
            intm_num = target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==intm_num:
                    return [i,j]

