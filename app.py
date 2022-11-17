from config import app
from apis.signup import signup_blueprint
from apis.signin import signin_blueprint
from apis.profile import profile_blueprint

app.register_blueprint(signup_blueprint)
app.register_blueprint(signin_blueprint)
app.register_blueprint(profile_blueprint)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')