class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nset = set()
        for num in nums:
            if num in nset:
                return True
            else:
                nset.add(num)
        return False


        