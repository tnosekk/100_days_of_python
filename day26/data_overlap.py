import pandas as pd

with open("day26/file1.txt", "r") as nums1:
    nums1_list = [int(num) for num in nums1.readlines()]


with open("day26/file2.txt", "r") as nums1:
    nums2_list = [int(num) for num in nums1.readlines()]

nums = [num for num in nums1_list if num in nums2_list]

print(nums)
