from API.extensions import db
from API.models.auth_model import LevelModel
from API import app

app.app_context().push()

tu = LevelModel('tata usaha')
guru = LevelModel('guru')
siswa = LevelModel('siswa')

db.session.add(tu)
db.session.add(guru)
db.session.add(siswa)
db.session.commit()