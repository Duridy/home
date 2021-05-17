kolvo = int(input())
gradysi = int(input())
otchimania = int(input())
class Oelg:
    heal = 100
    name = "Oleg"
    smoke = 5

    def __del__(self):

        print("Вся информация о 'Oleg' удалена")

    def __init__(self, heal):
        self.heal = self.heal - self.smoke * kolvo


    def stat(self):
        print("Здоровье стало =", str(self.heal) + '.' " Имя -", str(self.name) + '.' " Кол-во скуренных сигарет -",
              self.smoke)

class Yarik:
    heal = 100
    name = "Yaroslav"
    pit = 10

    def __init__(self, heal):
        self.heal = self.heal - self.pit * gradysi
    def stat(self):
        print("Здоровье стало =", str(self.heal) + '.' " Имя -", str(self.name) + '.' " Градусы -",
              self.pit)

class Ilya:
    heal = 100
    name = "Ilya"
    sport = 3

    def __init__(self, heal):
        self.heal = self.heal + self.sport * otchimania
    def stat(self):
        print("Здоровье стало =", str(self.heal) + '.' " Имя -", str(self.name) + '.' " Отжиманий -",
              self.sport)
oelg = Oelg(kolvo)
oelg.stat()

yarik = Yarik(gradysi)
yarik.stat()

ilya = Ilya(otchimania)
ilya.stat()
