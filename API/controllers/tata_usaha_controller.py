from API.lib.status_code import *
from API.models.tata_usaha_model import TuModel
from API.lib.database.db_custome import MyDB
from flask import Blueprint, jsonify, request

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/tambah-pegawai', methods=['POST','GET'])
def tambah_admin():
    nip = request.json.get('nip')
    nama_pegawai = request.json.get('nama_pegawai')
    gender = request.json.get('gender')
    alamat = request.json.get('alamat')
    telp = request.json.get('no_telp')
    pengguna_id = request.json.get('pengguna_id')



    sql = MyDB(TuModel(nama_pegawai,nip, gender, alamat, telp, pengguna_id))
    query = sql.filter_by(nip=nip)
    if query is not None:
        return jsonify({
            'error' : f'Data dengan nip : {nip}, sudah ada.'
        }), HTTP_409_CONFLICT


    sql.simpan()

    return jsonify({
        'id' : sql.table.id,
        'nama_pegawai' : sql.table.nama_pegawai,
        'jenis_kelamin' : sql.table.gender 
    }), HTTP_201_CREATED

