class Emperor:
  def __init__(self, name, birth, coronation, death):
    self.name = name
    self.birth = birth
    self.coronation = coronation
    self.death = death

charlemagne = Emperor("Charlemagne", 742, 800, 814)
print(vars(charlemagne))