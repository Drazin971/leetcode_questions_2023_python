class Solution:
  def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
      imax = len(img)
      jmax = len(img[0])
      def get_avg(i, j) -> int:
        t, c = 0, 0
        for idel in range(i-1, i+2):
          for jdel in range (j-1, j+2):
            if idel >= 0 and jdel >= 0 and idel < imax and jdel < jmax:
              t += img[idel][jdel]
              c += 1
        return t // c

      img_smoothed = [[0] * jmax for _ in range(imax)]

      for i in range(imax):
        for j in range(jmax):
          img_smoothed[i][j] = get_avg(i, j)

      return img_smoothed   


sol=Solution()

print(sol.imageSmoother(img = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))

print(sol.imageSmoother(img = [[100,200,100],[200,50,200],[100,200,100]])) # [[137,141,137],[141,138,141],[137,141,137]])