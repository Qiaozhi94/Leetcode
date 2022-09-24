nums = [-1,2,1,-4]
target = 1


ret = float('inf')
nums.sort()
length = len(nums)
for i in range(length - 2):
  left = i + 1
  right = length - 1
  while left < right:
    tmp = nums[i] + nums[left] + nums[right]
    ret = tmp if abs(tmp - target) < abs(ret - target) else ret
    if tmp == target:
      print(target)
    if tmp > target:
      right -= 1
    else:
      left += 1
print(ret)