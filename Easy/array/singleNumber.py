def singleNumber(nums):
    res = 0
    for x in nums:
        res^=x
    return res

nums = [2,2,1]
nums = singleNumber(nums)
print(nums)

"""XOR of a^b^a for some bits a and b returns b
a^b^a = (a^a)^b = 0^b = b
So we can XOR all bits together to find the unique number."""