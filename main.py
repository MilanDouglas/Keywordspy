class Emperor:
  def __init__(self, name, birth, coronation, death):
    self.name = name
    self.birth = birth
    self.coronation = coronation
    self.death = death

  def __str__(self):
    return (f"Emperor {self.name}, born in {self.birth},"
            f"was coronated in {self.coronation}, died in {self.death}")

charlemagne = Emperor("Charlemagne", 742, 800, 814)
print(charlemagne)