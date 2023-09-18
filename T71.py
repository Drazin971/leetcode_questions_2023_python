class Solution:
  def simplifyPath(self, path: str) -> str:

    p = []
    
    words = path.split("/")
   # print(words)

    for word in words:
      if word != '.' and word != '' and word != '..':
        p.append(word)

      if word == '..':
        if p:
          p.pop()

          
    return "/" + "/".join(p) 
  

sol=Solution()

print(sol.simplifyPath(path = "/home/")) #"/home"

print(sol.simplifyPath(path = "/../")) #"/"

print(sol.simplifyPath(path = "/home//foo/")) #"/home/foo"

print(sol.simplifyPath(path = "/a/b/../../c/")) #"/c"

print(sol.simplifyPath(path = "/..")) #"/"

print(sol.simplifyPath(path = "/....")) #"/..."'''

print(sol.simplifyPath(path = "/abc/...")) #"/abc/..."

print(sol.simplifyPath(path = "/a/../../b/../c//.//")) #"/c"

print(sol.simplifyPath(path = "/a/./b/../../c/")) #"/c"

print(sol.simplifyPath(path = "/home/foo/.ssh/../.ssh2/authorized_keys/")) #"/home/foo/.ssh2/authorized_keys"










 



