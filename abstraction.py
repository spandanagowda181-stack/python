from abc import ABC, abstractmethod
class greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass
class English(greet):
    def say_hello(self):
        return "hello"
e=English()
print(e.say_hello())