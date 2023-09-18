class Solution:
  def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
    n=len(dist)
    if hour<=n-1: return -1

    lo = 1
    hi = 1+max(max(dist), int(dist[-1]//(hour-n+1)))

    def time_needed(speed: int):
      sum = 0
      for i in dist[:-1]:
        sum += (i+speed-1)//speed
      sum += dist[n-1] / speed
      return sum

    speed=0
    while lo<=hi:
      mid = lo+(hi-lo)//2
      res = time_needed(mid)
      if res <= hour:
        hi = mid - 1
        speed = mid
      else:
        lo = mid + 1 
      
    return speed
    

sol=Solution()

#print(sol.minSpeedOnTime(dist = [1,3,2], hour = 6)) #1

#print(sol.minSpeedOnTime(dist = [1,3,2], hour = 2.7)) #3

#print(sol.minSpeedOnTime(dist = [1,3,2], hour = 1.9)) #-1

print(sol.minSpeedOnTime(dist = [1,1,100000], hour = 2.01)) #10000000




