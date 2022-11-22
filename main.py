from abc import ABC, abstractmethod
from typing import List


class Double(ABC):
    def __init__(self, massive: List[str]):
        self.massive = massive

    @abstractmethod
    def checking_double(self):
        pass

    @abstractmethod
    def deleting_double(self):
        pass

    def get_massive(self):
        return self.massive


class DoubleNearby(Double):
    def __init__(self, massive: List[str]):
        super().__init__(massive)

    def checking_double(self):
        counter = len(self.massive) - 1
        result = []
        for i in range(counter):
            if self.massive[i] == self.massive[i + 1]:
                result += [i, i + 1]
        return result

    def deleting_double(self):
        indexes_ignore = DoubleNearby.checking_double(self)
        if indexes_ignore:
            new_array = [x for i, x in enumerate(self.massive) if i not in indexes_ignore]
            self.massive = new_array
            return DoubleNearby.deleting_double(self)
        return self.massive


class DoubleOnTheSides(Double):
    def __init__(self, massive: List[str]):
        super().__init__(massive)

    def checking_double(self):
        return self.massive[0] == self.massive[-1]

    def deleting_double(self):
        if DoubleOnTheSides.checking_double(self):
            self.massive = self.massive[1:-1]
            DoubleOnTheSides.deleting_double(self)
        return self.massive


class DoubleSet(Double):
    def __init__(self, massive: List[str]):
        super().__init__(massive)

    def checking_double(self):
        pass

    def deleting_double(self):
        self.massive = set(self.massive)
        return self.massive


message1 = DoubleNearby(["a", "b", "b", "a", "z", "a", "a", "e", "z", "b", "a"])
message2 = DoubleOnTheSides(["a", "b", "b", "a", "z", "a", "a", "e", "z", "b", "a"])
message3 = DoubleSet(["a", "b", "b", "a", "z", "a", "a", "e", "z", "b", "a", "x"])

print(f"Массив #1 - {message1.get_massive()}")
print(f"Удаление дубликатов стоящих рядом в массиве - {message1.deleting_double()}\n")
print(f"Массив #2 - {message2.get_massive()}")
print(f"Удаление дубликатов стоящих по краям массива - {message2.deleting_double()}\n")
print(f"Массив #3 - {message3.get_massive()}")
print(f"Удаление не уникальных значений - {message3.deleting_double()}")
