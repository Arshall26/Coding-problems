"""Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores)."""

def removeDuplicates(nums):
    if(len(nums) == 0):
        return 0
    i = 1
    for j in range(1, len(nums)):
        if(nums[j] != nums[j-1]):
            nums[i] = nums[j]
            i +=1
    return i

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))