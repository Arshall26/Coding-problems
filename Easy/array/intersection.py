"""Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted."""

"""Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]"""


def intersection(nums1, nums2):
    output = []
    for x in nums1:
        if x in nums2:
            output.append(x)
            nums2.remove(x)
    return output



nums1, nums2 = [1,2,2,1], [2,2]
print(intersection(nums1, nums2))
