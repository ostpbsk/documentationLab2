from flask import Flask
from models.models import db
from dal.repositories import Repository
from dal.csv_reader import CSVReader
from bll.services import ImportService
from presentation.controller import ImportController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db.init_app(app)

with app.app_context():
    db.create_all()

    # DI
    repo = Repository()
    csv_reader = CSVReader()

    service = ImportService(repo, csv_reader)
    controller = ImportController(service)

    controller.import_data()