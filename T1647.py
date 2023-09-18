from collections import defaultdict

class Solution:
  def minDeletions(self, s: str) -> int:
    letters = defaultdict(int)
    for letter in s:
      letters[letter] += 1

    letter_counts = []
    
    for letter_count in letters.values():
      letter_counts.append(letter_count)

    letter_counts.sort()

    #print(letter_counts)

    sol = 0
    freq = {}
    for letter in letter_counts:
      while letter_counts.count(letter) in  1:
        letter -= 1
        sol += 1
      freq[letter] = 1

    return sol
      

sol = Solution()

#print(sol.minDeletions(s = "aab")) #0

print(sol.minDeletions("aaabbbcc")) #2

#print(sol.minDeletions(s = "ceabaacb")) #2

#print(sol.minDeletions(s = "accdcdadddbaadbc")) #1