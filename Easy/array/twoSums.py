"""Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."""

"""def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (nums[i] + nums[j] == target) and (i!=j):
                return i,j

nums = [10,15,2,7]
print(twoSum(nums, 9))"""

"""Usually, these kinds of problems can be solved by using a hash map.
   Loop through the list and add all the numbers in the hash with number as the key and index as the value. 
   Now loop through the list again and check the diff existence in the hash, and returns the indices."""


def twoSum(nums, target):
    _dict = {}
    for i, num in enumerate(nums):
        print(i,num)
        print(_dict.keys())
        print("target-num : ", target-num)
        if target-num in _dict.keys():
            return [_dict[target-num], i]
        else:
            _dict[num] = i

nums = [10,15,2,7]
print(twoSum(nums, 9))



