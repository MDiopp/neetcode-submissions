class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numhash = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in numhash:
                return [numhash[difference], i]
            numhash[nums[i]] = i