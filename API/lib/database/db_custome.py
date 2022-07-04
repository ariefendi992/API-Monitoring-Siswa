from this import d
from API.extensions import db

class MyDB:
    def __init__(self, table_name) -> None:
        self.table = table_name
    
    def simpan(self):
        data = self.table
        db.session.add(data)
        db.session.commit()

    def filter_by(self, *args, **kwargs):
        return self.table.query.filter_by(*args, **kwargs).first()

    def query_all(self):
        data = self.table.query.all()
        return data

    def query_update(self):
        return db.session.commit()

    def delete_query(self, *args ):
        db.session.delete(*args)
        db.session.commit()

    def join_one(self, *args):
        return db.session.query(self.table, *args).join(*args).all()

