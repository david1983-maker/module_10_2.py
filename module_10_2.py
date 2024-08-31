import time
from threading import Thread


class Knight(Thread):
    enemy = 100
    day = 1

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name},на нас напали!')
        while self.enemy > 1:
            self.enemy -= self.power
            time.sleep(1)
            if self.day == 1:
                print(f'{self.name} сражается {self.day} день, осталось {self.enemy} воинов')
            elif (self.day > 1) and (self.day < 5):
                print(f'{self.name} сражается {self.day} дня, осталось {self.enemy} воинов')
            else:
                print(f'{self.name} сражается {self.day} дней, осталось {self.enemy} воинов')
            self.day += 1

        print(f'{self.name} одержал победу спустя {self.day - 1} дней')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
