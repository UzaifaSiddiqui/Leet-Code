# -*- coding: utf-8 -*-
"""leetcode2441.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RszjO0GIv76UhgWU4aUUH3CbKpDIDvtu
"""

nums = [-1,2,-3,3]

def check(x , k):
  if k+x == 0:
      return k
  else:
    return 0

def function(nums):
  i = 0
  ans = -1
  while i<len(nums):
    k = max(nums)
    ans = list(map(lambda x:check(x,k), nums))
    if sum(ans) == 0:
      index = nums.index(k)
      nums[index] = 0
      i+=1
      ans = -1
    else:
      return k
  return ans

print(function(nums))

