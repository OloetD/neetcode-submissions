class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       count = collections.Counter(nums)
       sort = sorted(count.keys(), key=lambda x: count[x])
       return(sort[-k:])