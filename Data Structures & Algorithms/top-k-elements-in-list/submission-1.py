class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            if num in freq_map.keys():
                freq_map[num] +=1
            else:
                freq_map[num]=1
        li = sorted(freq_map.keys(), key=lambda x: freq_map[x])
        return li[-1:-k-1:-1]
