from API.extensions import db
from API.lib.custome.time_zone import utc_makassar
from slugify import slugify
from API.extensions import bcrypt

class AuthModel(db.Model):
    __tablename__ = 'tb_pengguna'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_pengguna = db.Column(db.String(128), nullable=False)
    slug = db.Column(db.String(128), nullable=False)
    kata_sandi = db.Column(db.String(256), nullable=False)
    kata_sandi_sekarang = db.Column(db.String(256), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('tb_level.id', ondelete='CASCADE', onupdate='CASCADE'),
                        nullable=False)
    created_at = db.Column(db.DateTime, default=utc_makassar())
    updated_at = db.Column(db.DateTime, onupdate=utc_makassar())

    def __init__(self, nama_pengguna, kata_sandi, level_id):
        self.nama_pengguna = nama_pengguna
        self.slug = slugify(nama_pengguna)
        self.kata_sandi = bcrypt.generate_password_hash(kata_sandi)
        self.kata_sandi_sekarang = kata_sandi
        self.level_id = level_id

    def __repr__(self):
        return f'id pengguna == {self.id}, nama pengguna == {self.nama_pengguna}'

    def generate_pw_hash(kata_sandi):
        return bcrypt.generate_password_hash(kata_sandi)

    def check_pw_hash(*args, **kwargs):
        return bcrypt.check_password_hash(*args, **kwargs)


class LevelModel(db.Model):
    __tablename__ = 'tb_level'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.String(64), nullable=False)  

    def __init__(self, level) -> None:
        super().__init__()
        self.level = level

    def __repr__(self):
        return 'id = {}, level pengguna = {}'.format(self.id, self.level)