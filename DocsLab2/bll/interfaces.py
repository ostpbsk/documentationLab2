from abc import ABC, abstractmethod

class IDataImportService(ABC):

    @abstractmethod
    def import_data(self, file_path):
        pass