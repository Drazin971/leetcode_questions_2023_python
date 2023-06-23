class Solution:
  def convert(self, s: str, numRows: int) -> str:
    converted_array = []
    
    pos, x, y = 0,0,0
    news_s=""
    
    down_direction = True # True - tam  False - z powrotem
    while pos<len(s):
      converted_array.append((y,pos))
      
      if down_direction:
        y+=1
        if y==numRows-1:
          down_direction=False
      else:
        y-=1
        x+=1
        if y==0:
          down_direction=True
      
      pos+=1

    converted_array.sort()
    
    for i, j in converted_array:
      news_s = news_s + s[j]
    
    return news_s



sol=Solution()

print(sol.convert(s = "PAYPALISHIRING", numRows = 3)) #"PAHNAPLSIIGYIR"

print(sol.convert(s = "PAYPALISHIRING", numRows = 4 )) #"PINALSIGYAHRPI"