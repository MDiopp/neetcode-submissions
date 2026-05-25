class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        currNum = 0
        numsToLoop = 0
        numProducts = {}
        output = []
        for num in nums:
            numProducts[currNum] = 1
            if(currNum == 0):
                currNum += 1
                continue
            numsToLoop = currNum 
            numProducts[currNum] = 1 * numProducts[currNum - 1] * nums[currNum - 1]
            for i in range(numsToLoop):
                numProducts[i] = numProducts[i] * nums[currNum]
            
            currNum = numsToLoop + 1
        for i in range(currNum):
            output.append(numProducts[i])
        return output

        