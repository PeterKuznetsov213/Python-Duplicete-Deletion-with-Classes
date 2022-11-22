from abc import ABC, abstractmethod
from typing import List


# m = ["a", "z", "a", "b", "b", "a", "z", "a", "a", "e", "z", "a"]


# def delete_double(m: List[str]) -> List:
#     indexes_ignore = check_double(m)
#
#     if indexes_ignore:
#         new_array = [x for i, x in enumerate(m) if i not in indexes_ignore]
#         return delete_double(new_array)
#     return m


# def check_double(m: List[str]) -> List[int]:
#     counter = len(m) - 1
#     result = []
#     for i in range(counter):
#         if m[i] == m[i + 1]:
#             result += [i, i + 1]
#     return result
#
# print(delete_double(m))

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
        print(self.massive)


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
            self.massive=new_array
            return DoubleNearby.deleting_double(self)
        return self.massive


message = DoubleNearby(["a", "z", "a", "b", "b", "a", "z", "a", "a", "e", "z", "a"])
# print(message.checking_double())
print(message.deleting_double())
# class Dog(ABC):
#     def __init__(self, name: str, age: int):
#         self.age = age
#         self.name = name
#
#
#     def get_name(self):
#         print(self.name)
#
#     @abstractmethod
#     def eat(self):
#         pass
#
#
# class Taksa(Dog):
#
#     def __init__(self, name: str, age: int):
#         super().__init__(name, age)
#
#     def eat(self):
#         return "я ем"
#
#
#
# dog = Taksa("dagy", 22)
# print(dog.get_name())
# dog.weight = 15
# print(dog.weight, dog.eat())
