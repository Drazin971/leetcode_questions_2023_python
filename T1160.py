class Solution:
  def countCharacters(self, words: list[str], chars: str) -> int:
    res = 0
    dic = {}
    for char in chars:
      if char not in dic:
        dic[char] = 1
      else:
        dic[char] += 1
            
    for word in words:
      found = True
      d = {}
      for letter in word:
        if letter not in d:
          d[letter] = 1
        else:
          d[letter] += 1
        if letter not in dic or d[letter] > dic[letter]: 
          found = False
          break
      if found: res += len(word)

    return res

sol=Solution()

print(sol.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr")) # 10