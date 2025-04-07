class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                #print(i) //comprobar que este bien
                return i
        return len(nums)
            
'''sol = Solution()
numeros = [0, 1, 3]
sol.missingNumber(numeros)'''