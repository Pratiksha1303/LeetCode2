# LEETCODE


# class Solution(object):
#     def plusOne(self, digits):
#         num = int("".join(map(str, digits)))
#         num += 1
#         return [int(digit) for digit in str(num)]


arr = [9, 9, 9]

num = int("".join(map(str, arr)))  
nums = num + 1                     

result = [int(digit) for digit in str(nums)]

print(result)  #OUTPUT: [1,0,0,0]