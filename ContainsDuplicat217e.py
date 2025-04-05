class Solution(object):
    def containsDuplicate(self, nums):
        if len(set(nums)) !=len(nums):
            return True
        else:
            return False
    
'''
class Solution(object):
    def containsDuplicate(self, nums):
        if len(set(nums)) !=len(nums):
            return print("False")
        else:
            return print("True")
    
sol=Solution()
print(sol.containsDuplicate([1,2,3,4,5,5]))
//prueba para mi
'''
