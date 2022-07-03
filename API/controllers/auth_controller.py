from flask import Blueprint
from API.models.auth_model import AuthModel, RoleModel

auth = Blueprint('auth',__name__, url_prefix='/auth')
