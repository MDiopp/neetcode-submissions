class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}
        output = []
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        for i in range(len(nums)):
            occurences[nums[i]] = 1 + occurences.get(nums[i], 0)
        for i in range(0, k):
            largest_key = max(occurences, key=occurences.get)
            output.append(largest_key)
            occurences.pop(largest_key)
        return output
        
        
        