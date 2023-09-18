class Solution:
  def wordBreak(self, s: str, wordDict: list[str]) -> bool:

    wf = [False] * (len(s) + 1)
    wf[len(s)] = True

    for i in range(len(s)-1,-1,-1):
      for w in wordDict:
        if (i+len(w))<=len(s) and s[i: i + len(w)] == w:
          wf[i]=wf[i + len(w)]
        if wf[i]:
          break
  
    return wf[0]
      
    

sol=Solution()

print(sol.wordBreak(s = "leetcode", wordDict = ["leet","code"])) #True

print(sol.wordBreak(s = "applepenapple", wordDict = ["apple","pen"])) #True

print(sol.wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"])) #False

print(sol.wordBreak(s = "catsanddog", wordDict = ["cats","dog","sand","and","cat"])) #True



