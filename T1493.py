  def minSubArrayLen(self, target: int, nums: list[int]) -> int:
    p1, p2 = 0, len(nums)-1
    sum_of_nums = sum(nums)

    if sum_of_nums < target: return 0

    while sum_of_nums>target:
      #print(sum_of_nums, p1, p2)
      if nums[p1]<=nums[p2]:
        sum_of_nums-=nums[p1]
        p1+=1
      else:
        sum_of_nums-=nums[p2]
        p2-=1
    #print("solution", sum_of_nums, p1, p2)
    return p2-p1+1 if sum_of_nums>=target else p2-p1+2
     
         