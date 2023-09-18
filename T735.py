class Solution:
  def asteroidCollision(self, asteroids: list[int]) -> list[int]:
    sol = []

    for ast in asteroids:
      if not sol or ast>0:
          sol.append(ast)
      else:
        while sol and sol[-1]>0 and sol[-1]<abs(ast):
          sol.pop() 
      
        if sol and sol[-1]==abs(ast):
          sol.pop()
        else:
          if not sol or sol[-1]<0:
            sol.append(ast)
          
    return sol


sol = Solution()

r=sol.asteroidCollision(asteroids = [5,10,-5]) #[5,10]

print(r)

r=sol.asteroidCollision(asteroids = [8,-8]) #[]

print(r)

r=sol.asteroidCollision(asteroids = [10,2,-5]) #[10]

print(r)

r=sol.asteroidCollision(asteroids = [-2,-1,1,2]) #[-2,-1,1,2]

print(r)