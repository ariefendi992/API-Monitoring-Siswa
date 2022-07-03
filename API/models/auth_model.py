from API.extensions import db
from API.lib.time_zone import utc_makassar

class AuthModel(db.Model):
    __tablename__ = 'tb_pengguna'
    id_pengguna = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_pengguna = db.Column(db.String(128), nullable=False)
    kata_sandi = db.Column(db.String(256), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('tb_role.id_role', ondelete='CASCADE', onupdate='CASCADE'),
                        nullable=False)
    created_at = db.Column(db.DateTime, default=utc_makassar())
    updated_at = db.Column(db.DateTime, onupdate=utc_makassar())
    role = db.relationship('tb_role', backref=db.backref('tb_pengguna', lazy=True))

    def __repr__(self):
        return f'id pengguna == {self.id_pengguna}, nama pengguna == {self.nama_pengguna}'


class RoleModel(db.Model):
    __tablename__ = 'tb_role'
    id_role = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(64), nullable=False)  

    def __repr__(self):
        return 'id = {}, role = {}'.format(self.id_role, self.role)