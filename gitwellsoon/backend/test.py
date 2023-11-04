from sshtunnel import SSHTunnelForwarder
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)

# Create an SSH tunnel
with SSHTunnelForwarder(
    ('ec2-18-142-239-91.ap-southeast-1.compute.amazonaws.com'),
    ssh_username="ec2-user",
    ssh_pkey="gitwellsoon-is458.pem",
    remote_bind_address=('gitwellsoon.cqglyyh818jk.ap-southeast-1.rds.amazonaws.com', 3306)
) as tunnel:
    print("****SSH Tunnel Established****")
    
    # Define your Flask app configuration for the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:Hellocloudy!@127.0.0.1:{}/gitwellsoon'.format(tunnel.local_bind_port)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Create a SQLAlchemy database instance
    db = SQLAlchemy(app)

    # Your database models (Accounts, Products, Orders) and their definitions go here
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
        def __init__(self, pcat, pname, pdesc, img_src, pprice, stock, prod_date, expiry_date):
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

    @app.route('/accounts', methods=['GET'])
    def get_all_accounts():
        accounts = Accounts.query.all()
        account_list = [{'username': acc.username, 'email': acc.email} for acc in accounts]
        return jsonify(account_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
