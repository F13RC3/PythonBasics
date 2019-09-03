class Enemy:
    life=3

    def __init__(self):
        print("I am like a Constructor")

    def attack(self):
        print("ouch!")
        self.life -=1

    def checkLife(self):
        if self.life<=0:
            print("You r DED!")
        else:
            print(str(self.life)+" Life Left")

class Saviour(Enemy):
    pass

enemy1 = Saviour()
enemy2 = Saviour()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()