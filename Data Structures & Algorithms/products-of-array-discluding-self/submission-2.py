class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        currNum = 0
        numsToLoop = 0
        remainingProduct = 1
        numProducts = {}
        output = []
        for num in nums:
            numProducts[currNum] = 1
            if(currNum == 0):
                currNum += 1
                continue
            numProducts[currNum] = 1 * numProducts[currNum - 1] * nums[currNum - 1]
            currNum = currNum + 1
        numsToLoop = currNum 
        currNum -= 1
        remainingProduct =  nums[currNum]
        for i in range(numsToLoop - 2, -1, -1):
            numProducts[i] = numProducts[i] * remainingProduct
            currNum -= 1
            remainingProduct = remainingProduct * nums[currNum]
        currNum = numsToLoop
        for i in range(currNum):
            output.append(numProducts[i])
        return output

        