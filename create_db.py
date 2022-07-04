from API import app
from API.extensions import db
from API.models.auth_model import LevelModel

def app_context():
    return app.app_context().push()

def create_all():
    return db.create_all()

def drop_all():
    return db.drop_all()

def create_level():
    admin = LevelModel('admin')
    guru = LevelModel('guru')
    siswa = LevelModel('siswa')

    db.session.add(admin)
    db.session.add(guru)
    db.session.add(siswa)
    db.session.commit()

def query_level():
    data = LevelModel.query.all()

    for i in data:
        print(i['id'] + '||' + i['level'])

