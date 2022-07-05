from API.extensions import db
from API.lib.custome.time_zone import utc_makassar
from slugify import slugify

class TuModel(db.Model):
    __tablename__ = 'tb_tu'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nip = db.Column(db.String(32), nullable=True)
    nama_pegawai = db.Column(db.String(128), nullable=False)
    slug = db.Column(db.String(256), nullable=False)
    gender = db.Column(db.String(32), nullable=True)
    alamat = db.Column(db.String(256), nullable=True)
    telp = db.Column(db.String(16), nullable=True)
    pengguna_id = db.Column(db.Integer, db.ForeignKey('tb_pengguna.id', 
                            ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    created_at = db.Column(db.DateTime, default=utc_makassar())
    updated_at = db.Column(db.DateTime, onupdate=utc_makassar())

    def __init__(self, nama_pegawai, nip='', gender='', alamat='', telp='', pengguna_id ='' ) -> None:
        super().__init__()
        self.nip = nip
        self.nama_pegawai = nama_pegawai
        self.slug = slugify(nama_pegawai)
        self.gender = gender,
        self.alamat = alamat,
        self.telp = telp
        self.pengguna_id = pengguna_id

    def __repr__(self) -> str:
        return '[(id : {}, nama : {}, gender : {})]'.format(self.id, self.nama_pegawai, self.gender)




