"""Given an integer array nums, return true if any value appears 
at least twice in the array, and return false if every element is distinct."""

"""Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false"""

#solution mais a une complexité trop grande O(n^2)
"""def containsDuplicate(nums):
    for i in range(len(nums)):
        index = nums[i]
        for j in range(len(nums)):
            if (nums[j] == index and j != i):
                return True
    return False"""

#meilleure solution que la précédente on met le tableau dans un set qui enleve directement les doublons
#on a ensuite juste à faire un test sur la taille des deux objets
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

nums = [1,2,3,1]
print(containsDuplicate(nums))


nums = [1,2,3,4]
print(containsDuplicate(nums))
