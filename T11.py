class Solution:
    def maxArea(self, height: list[int]) -> int:

      def get_Area(a,b) -> int:
        nonlocal height
        return min(height[b],height[a])*(b-a)
        
      start, end = 0, len(height)-1
      curr_area = 0

      while start<end:
        print(height[start],height[end])
        curr_area=get_Area(start,end) if get_Area(start,end)>curr_area else curr_area
        if height[start]<height[end]:
          start+=1
        else:
          end-=1
      
        
      return curr_area
      
    
     
sol=Solution()

print(sol.maxArea(height = [1,8,6,2,5,4,8,3,7])) #49
print(sol.maxArea(height = [1,1])) #1
print(sol.maxArea(height = [2,3,4,5,18,17,6])) #17
