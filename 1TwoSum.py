class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """ 
        hash={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in hash:
                return [hash[diff], i]
            hash[n]=i
        return


sol=Solution()
resultado=sol.twoSum([2,7,11,15], 9)
print(resultado)
