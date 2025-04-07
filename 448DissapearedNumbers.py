class Solution(object):
    def findDisappearedNumbers(self, nums):
        ret=[]
        num_set=set(nums)
        for i in range (1,len(nums)+1):
            if i not in num_set:
                ret.append(i)
        return ret



sol=Solution()
resultado=sol.findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(resultado)