class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

      nums.sort()
      a = len(nums)
      if a > 1:
        for i in range(a):
            if nums[i] == nums[i-1]:
                return True
                break
            else:
                continue
        return False
      else:
        return False
