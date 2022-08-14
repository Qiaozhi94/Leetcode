nums = [-1,0,1,2,-1,-4]
list_total= []

if len(nums) < 3:
  print("[]")
if len(nums) >= 3:
  for a in range(len(nums)-2):
    for b in range(a + 1, len(nums)-1):
      for c in range(b + 1, len(nums)):
        list = []
        if nums[a] + nums[b] + nums[c] == 0:
          list.append(nums[a])
          list.append(nums[b])
          list.append(nums[c])
          list.sort()
          if list not in list_total:
            list_total.append(list)
          else:
            continue
        else:
          continue
  print(list_total)