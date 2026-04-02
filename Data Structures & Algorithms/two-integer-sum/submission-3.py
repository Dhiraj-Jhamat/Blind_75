class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in hm.keys():
                return [hm.get(temp),i]
            hm[nums[i]]=i
        return