class FoodRatings:

  def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
      self.f = []
      for i in range(len(foods)):
          self.f.append((foods[i], cuisines[i], ratings[i]))
      self.f.sort(key = lambda x: x[0])

  def changeRating(self, food: str, newRating: int) -> None:
      for i in range(len(self.f)):
        dish = self.f[i]
        if dish[0] == food:
          self.f[i] = (dish[0], dish[1], newRating)

  def highestRated(self, cuisine: str) -> str:
    hdish = []
    for dish in self.f:
      if dish[1] == cuisine:
        hdish.append((dish[0], dish[2]))

    hdish.sort(key = lambda x: x[1], reverse=True)
   # print(hdish)
    return hdish[0][0]


fr = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7])

print(fr.highestRated("korean"))
print(fr.highestRated("japanese"))
print(fr.changeRating("sushi", 16))
print(fr.highestRated("japanese"))
print(fr.changeRating("ramen", 16))
print(fr.highestRated("japanese"))

