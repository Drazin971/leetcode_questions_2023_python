class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
      sorted_cookies = cookies.sort(reverse=True)
      cookie_table = [0]*k

      print(sorted_cookies)

      def distribute(cookies:list[int], k: int):
        if k==1: return sum(cookies) 
        avg = sum(cookies) // k
        
          
      return cookies

sol=Solution()

print(sol.distributeCookies(cookies = [8,15,10,20,8], k = 2)) #31

print(sol.distributeCookies(cookies = [6,1,3,2,2,4,1,2], k = 3)) #7