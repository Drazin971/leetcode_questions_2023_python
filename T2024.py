class Solution:
  def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
    c = {"T":0,"F":0}
    i = 0
    ans=0

    for j in range(len(answerKey)):
      c[answerKey[j]]+=1
      while c["T"]>k and c["F"]>k:
        c[answerKey[i]]-=1
        i+=1
      ans = max(ans, j-i+1)
    
    return ans


     
sol=Solution()

print(sol.maxConsecutiveAnswers(answerKey = "TTFTTFTT", k = 1)) #Output: 5

print(sol.maxConsecutiveAnswers(answerKey = "TFFTTTT", k = 2)) #Output: 7

print(sol.maxConsecutiveAnswers(answerKey = "TTFF", k = 2)) #Output: 4

print(sol.maxConsecutiveAnswers(answerKey = "TFFT", k = 1)) #Output: 3
