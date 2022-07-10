class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = len(nums)
        b = 0 

        for i in range(a):
            for m in range(a):
                if i == m:
                    m = m + 1
                else:
                    if nums[i] == nums[m]:
                        b = b + 1
                        m = m + 1
                    else:
                        m = m + 1
            i = i + 1


        if b >= 2:
            return True

        else: 
            return False