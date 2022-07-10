nums = [2, 3, 1, 0, 2, 5, 3]
nums.sort()
print(nums)


left = 0

while left < len(nums) - 1:
  if nums[left] == nums[left + 1]:
    print(nums[left])
    break
  elif nums[left] != nums[left + 1]:
    left = left + 1


