from API.controllers.auth_controller import auth
from API.controllers.tata_usaha_controller import admin
from API.controllers.guru_controller import guru

def register_app(app):
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(guru)