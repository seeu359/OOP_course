"""
Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса
должны создаваться командой:

dt = DeltaClock(clock1, clock2)

где clock1, clock2 - объекты другого класса Clock для хранения текущего
времени. Эти объекты должны создаваться командой:

clock = Clock(hours, minutes, seconds)

где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные
числа).

В классе Clock также должен быть (по крайней мере) один метод (возможны и
другие):

get_time() - возвращает текущее время в секундах (то есть, значение
hours * 3600 + minutes * 60 + seconds).

После создания объекта dt класса DeltaClock, с ним должны выполняться команды:

str_dt = str(dt)   # возвращает строку разницы времен clock1 - clock2 в
формате: часы: минуты: секунды
len_dt = len(dt)   # разницу времен clock1 - clock2 в секундах (целое число)
print(dt)   # отображает строку разницы времен clock1 - clock2 в формате:
часы: минуты: секунды

Если разность получается отрицательной, то разницу времен считать нулевой.
"""

from time import strftime, gmtime


class DeltaClock:

    def __init__(self, clock1, clock2):

        self.clock1: Clock = clock1
        self.clock2: Clock = clock2

    def __str__(self):
        if self.clock1.get_time() < self.clock2.get_time():
            return '00: 00: 00'
        return strftime('%H: %M: %S',
                        gmtime(self.clock1.get_time() -
                               self.clock2.get_time()))

    def __len__(self):
        time_delta = self.clock1.get_time() - self.clock2.get_time()
        if time_delta > 0:
            return time_delta
        return 0


class Clock:

    MINUTES_IN_HOURS = 60
    SECONDS_IN_HOURS = 3600

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> int:
        return self.hours * self.SECONDS_IN_HOURS + \
            self.minutes * self.MINUTES_IN_HOURS + self.seconds
