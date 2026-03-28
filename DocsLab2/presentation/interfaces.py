from abc import ABC, abstractmethod

class IImportController(ABC):

    @abstractmethod
    def import_data(self): pass