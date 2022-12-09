
class TVProgram:

    def __init__(self, name):
        self.name = name
        self.items = list()

    def add_telecast(self, tl):
        self.items.append(tl)

    def remove_telecast(self, indx):
        for item in self.items:
            if item.uid == indx:
                self.items.remove(item)


class Telecast:

    def __init__(self, id, name, duration):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration
