# LEETCODE


# class Solution:
#     def intersection(self, nums1, nums2):
#         result = []
#         for i in nums1:
#             if i in nums2 and i not in result:
#                 result.append(i)
#         return result


num1 = [1,2,2,1]
num2 = [2,2]
result = []

for i in num1:
    if i in num2 and i not in result: 
        result.append(i)

print(result)  


# OUTPUT: [2]