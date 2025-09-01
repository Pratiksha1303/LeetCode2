# LEETCODE


# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
       
#         res = nums1[:m] + nums2[:n]
#         res.sort()
        
#         for i in range(len(res)):
#             nums1[i] = res[i]


#SOLUTION-1


# a1 = [1, 2, 3, 7, 8, 9, 10]
# a2 = [0, 11, 12, 4, 5, 6]

# m = 3
# n = 3

# res = []

# for i in range(len(a1)):
#     if i == m:  
#         break
#     res.append(a1[i])


# for j in range(len(a2)):
#     if j == n:
#         break
#     res.append(a2[j])


# res.sort()

# print(res)   # Output: [0, 1, 2, 3]


#SOLUTION-2


a1 = [1, 2, 3, 7, 8, 9, 10]
a2 = [0, 11, 12, 4, 5, 6]

m = 3
n = 3


res = a1[:m] + a2[:n]

res.sort()

print(res)   # Output: [0, 1, 2, 3]
