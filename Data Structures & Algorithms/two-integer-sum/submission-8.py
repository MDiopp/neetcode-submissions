class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nhash = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nhash:
                return [nhash[difference], i]
            nhash[nums[i]] = i

