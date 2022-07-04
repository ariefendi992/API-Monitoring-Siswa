from flask import Blueprint, jsonify, request
from API.extensions import db
from API.lib.database.db_custome import MyDB
from API.lib.status_code import *
from API.models.auth_model import AuthModel, LevelModel
from API.extensions import jwt

auth = Blueprint('auth',__name__, url_prefix='/auth')


@jwt.user_identity_loader
def user_identity(user):
    return user.id

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return AuthModel.query.filter_by(id=identity).one_or_none()

@auth.route('/register-user', methods=['GET','POST'])
def tambah_pengguna():
    nama_pengguna = request.json.get('username')
    kata_sandi = request.json.get('password')
    level_id = request.json.get('level')        

    if len(kata_sandi) < 6:
        return jsonify(
            {
                'error' : 'Kata sandi minimal 6 karakter'
            }
        ), HTTP_400_BAD_REQUEST

    
    query = MyDB(AuthModel(nama_pengguna, kata_sandi, level_id))

    if query.filter_by(nama_pengguna=nama_pengguna) is not None:
        return jsonify({
            'error' : f'Akun dengan username {nama_pengguna} sudah ada.'
        }), HTTP_400_BAD_REQUEST

    query.simpan()

    return jsonify({
        'id' : query.table.id,
        'username' : query.table.nama_pengguna,
        'slug' : query.table.slug
    }), HTTP_201_CREATED


@auth.route('/data-pengguna', methods=['GET'])
def fecth_data_pengguna():    
    query = MyDB(AuthModel)
    query_join = query.join_one(LevelModel)

    data = []
    for j, l in query_join:
        data.append({
            'id' : j.id,
            'username' : j.nama_pengguna,
            'level' : l.level
        })    
   
    return jsonify({
        'data' : data
    }), HTTP_200_OK

@auth.put('/edit-pengguna')
@auth.patch('/edit-pengguna')
@auth.get('/edit-pengguna')
def edit_pengguna():    
    nama_penguna = request.json.get('username')
    kata_sandi = request.json.get('password')
    level_id = request.json.get('level')

    slug = request.args.get('slug')
    query = MyDB(AuthModel)
    sql = query.filter_by(slug=slug)

    print(sql.nama_pengguna)

    sql.nama_pengguna = nama_penguna
    sql.kata_sandi = AuthModel.generate_pw_hash(kata_sandi)
    sql.kata_sandi_sekarang = kata_sandi
    sql.level_id = level_id

    query.query_update()

    return jsonify({
        'id' : sql.id,
        'username' : sql.nama_pengguna,
        'slug' : sql.slug
    }), HTTP_201_CREATED