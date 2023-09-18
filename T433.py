from collections import deque

class Solution:
  def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
    q=deque()
    q.append([startGene,0])
    visited = set()

    def is_mutable(startGene: str, endGene) -> bool:
      diff=0
      for i in range(8):
        if startGene[i] != endGene[i]:
          diff+=1
          if diff>1: return False
      return True if diff==1 else False
      
    while q:
      curent_gene, change_count = q.popleft()
      visited.add(curent_gene)
      for gene_from_bank in bank:
        if is_mutable(curent_gene, gene_from_bank) and gene_from_bank not in visited:
          if gene_from_bank==endGene: return change_count+1
          q.append([gene_from_bank, change_count+1])
    return -1
                     
sol = Solution()

r=sol.minMutation(startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]) #1

print(r)

r=sol.minMutation(startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]) #2

print(r)