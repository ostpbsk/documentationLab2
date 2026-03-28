from presentation.interfaces import IImportController

class ImportController(IImportController):

    def __init__(self, service):
        self.service = service

    def import_data(self):
        self.service.import_data("data/data.csv")