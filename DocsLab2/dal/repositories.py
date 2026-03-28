from models.models import db
from dal.interfaces import IRepository

class Repository(IRepository):
    def add(self, obj):
        db.session.add(obj)
        db.session.commit()