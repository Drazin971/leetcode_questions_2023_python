class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
      if (coordinates[1][0] - coordinates[0][0]) !=0:
        a = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        b = coordinates[0][1]-a*coordinates[0][0]
      else:
        b=coordinates[0][0]
        for point in coordinates:
          if point[0]!=b:
            return False
        return True
          
      

      #print(a,b)
      for point in coordinates:
        if point[1] != a*point[0]+b:
          print(point[1],a*point[0]+b)
          return False
      return True
      
        


sol = Solution()

#print(sol.findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]]))

print(sol.checkStraightLine(coordinates = [[0,0],[0,5],[5,5],[5,0]]))