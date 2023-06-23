class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
      for i in range(m,n+m):
        nums1[i]=nums2[n+m-i-1]
      nums1.sort()
      print(nums1)

sol = Solution()



print(sol.merge(nums1 = [1,2,4,5,6,0], m = 5, nums2 = [1], n = 1))