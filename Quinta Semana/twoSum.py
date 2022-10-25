class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in nums:
                if i != nums.index(num2):
                    return [i, nums.index(num2)]
        


        
        
        
        
        
""" 
for i in range(len(nums)):
            index = 0
            while index < len(nums):
                if nums[i] == nums[index]:
                    index += 1
                if nums[i] + nums[index] == target:
                       return [i, index]
                index += 1
"""

"""
for i in range(len(nums)):
    num2 = target - nums[i]
        if num2 in nums:
            return [i, nums.index(num2)]
            


for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    if i != j:
                        return[i, j]


"""