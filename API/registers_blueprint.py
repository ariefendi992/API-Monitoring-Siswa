from API.controllers.auth_controller import auth

def register_app(app):
    app.register_blueprint(auth)