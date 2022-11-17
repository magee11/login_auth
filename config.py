from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask import Flask
from flask_mail import Mail, Message


app = Flask(__name__)
JWTManager(app)
mail = Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
app.config['SECRET_KEY'] = '237748fd-4a48-4818-8b9c-04a9cd754e65'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:PWA_DB$iphone_21@localhost/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)



