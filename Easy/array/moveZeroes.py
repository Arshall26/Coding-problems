"""Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]"""

"""PREMIER TRUC QUE TU FAIS BIEN et sur leetcode ils disent que c faux mais c bon"""

def moveZeroes(nums):
    for i in range(len(nums)):
        if(nums[i]==0):
            nums = nums + nums[i:i+1]
            nums.remove(nums[i])
    return nums

   


nums = [0,1,0,3,12]
print(moveZeroes(nums))

nums = [0]
print(moveZeroes(nums))

nums = [0,1,0,0,0,5,8,80,0,41,0,0,1,1,2]
print(moveZeroes(nums))



