from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import platform

app = Flask(__name__)

# DO NOT REMOVE
print(platform.system())
if platform.system() == "Darwin":
    # FOR MAC USERS
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/gitwellsoon'
else:
    # FOR WINDOWS USERS
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/gitwellsoon'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Accounts(db.Model):
    __tablename__ = "accounts"

    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), primary_key=True)
    Orders = db.relationship('Orders', backref='accounts', lazy=True, passive_deletes=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class Products(db.Model):
    __tablename__ = "products"
    def __init__(self, pid, pcat, pname, pdesc, img_src, pprice, stock, prod_date, expiry_date):
        self.pid = pid
        self.pcat = pcat
        self.pname = pname
        self.pdesc = pdesc
        self.img_src = img_src
        self.pprice = pprice

        self.stock = stock
        self.prod_date = prod_date
        self.expiry_date = expiry_date

    pid = db.Column(db.Integer, primary_key=True)
    pcat = db.Column(db.String(255), nullable=False)
    pname = db.Column(db.String(255), nullable=False)  
    pdesc = db.Column(db.String(255), nullable=False)  
    img_src = db.Column(db.String(255), nullable=False)  
    pprice = db.Column(db.Integer, nullable=False)  
    stock = db.Column(db.Integer, nullable=False)  
    prod_date = db.Column(db.Date, nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)
    Orders = db.relationship('Orders', backref='products', lazy=True, passive_deletes=True)

class Orders(db.Model):
    __tablename__ = "orders"
    def __init__(self, oid, email, pid, quantity):
        self.oid = oid
        self.email = email
        self.pid = pid
        self.quantity = quantity

    oid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), db.ForeignKey('accounts.email'),nullable=False)  
    pid = db.Column(db.Integer, db.ForeignKey('products.pid'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)