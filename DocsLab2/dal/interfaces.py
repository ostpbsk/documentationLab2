from abc import ABC, abstractmethod

class IRepository(ABC):
    @abstractmethod
    def add(self, obj): pass

class ICSVReader(ABC):
    @abstractmethod
    def read(self, path): pass