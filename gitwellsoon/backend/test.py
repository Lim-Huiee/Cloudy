from sshtunnel import SSHTunnelForwarder
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)
# Create an SSH tunnel
# with SSHTunnelForwarder(
#     ssh_address_or_host=('ec2-18-142-239-91.ap-southeast-1.compute.amazonaws.com'),
#     ssh_username="ec2-user",
#     ssh_password="",
#     ssh_pkey="gitwellsoon-is458.pem",
#     remote_bind_address=('gitwellsoon.cqglyyh818jk.ap-southeast-1.rds.amazonaws.com', 3306),
#     local_bind_address=("127.0.0.1", 63467)
# ) as tunnel:
#     print("****SSH Tunnel Established****")
tunnel = SSHTunnelForwarder(
    ('ec2-13-213-40-123.ap-southeast-1.compute.amazonaws.com', 22),
    ssh_username="ec2-user",
    ssh_password="",
    ssh_pkey="gitwellsoon-is458.pem",
    remote_bind_address=('gitwellsoon.cqglyyh818jk.ap-southeast-1.rds.amazonaws.com', 3306),
    )

tunnel.start()
print("SSH connection created..")

# Define your Flask app configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admin:Hellocloudy!@127.0.0.1:{}/gitwellsoon".format(tunnel.local_bind_port)
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
    def __init__(self, email, pid, quantity, status):
        self.email = email
        self.pid = pid
        self.quantity = quantity
        self.status= status

    oid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), db.ForeignKey('accounts.email'),nullable=False)  
    pid = db.Column(db.Integer, db.ForeignKey('products.pid'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=False)


#ACCOUNTS
@app.route('/accounts', methods=['GET'])
def get_all_accounts():
    accounts = Accounts.query.all()
    account_list = [{'username': acc.username, 'email': acc.email} for acc in accounts]
    return jsonify(account_list)

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = Accounts.query.filter_by(email=email).first()

        if not user:
            return jsonify({ "code": 401, "message": "No such account"}), 401 

        if user and check_password_hash(user.password, password):
            return jsonify({"code": 200, "email": email}), 200 

        return jsonify({ "code": 401, "message": "incorrect email or password"}), 401
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/create_account', methods=['POST'])
def createAccount():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        user = Accounts.query.filter_by(email=email).first()

        if user:
            return jsonify({"code": 409, "message": "User already exist"}), 409            
        
        password_hash = generate_password_hash(password, "sha256")

        new_user = Accounts(
            username=username, 
            email=email,
            password=password_hash)
        
        db.session.add(new_user)
        db.session.commit()

        return jsonify({ "code": 200, "message": "Success"}), 200 

    except Exception as e:
        return jsonify({'error': str(e)}), 500

#PRODUCTS
@app.route('/product_list', methods=['GET'])
def get_all_products():
    try:

        products = Products.query.all()
        products_list = []
        for product in products:
            product_obj = {
                'pid': product.pid,
                'pcat': product.pcat,
                'pname': product.pname,
                'pdesc': product.pdesc,
                'img_src': product.img_src,
                'pprice': product.pprice,
                'stock': product.stock,
                'prod_date': product.prod_date.strftime('%Y-%m-%d'),
                'expiry_date': product.expiry_date.strftime('%Y-%m-%d')
            }

            products_list.append(product_obj)
        
        return jsonify({"code": 200, "data": products_list}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

 
@app.route('/create_product', methods=['POST'])
def create_product():
    try: 
        data = request.get_json()
        pcat = data.get('pcat')
        pname = data.get('pname')
        pdesc = data.get('pdesc')
        pprice = data.get('pprice')
        pstock = data.get('stock')
        prod_date = data.get('prod_date')
        expiry_date = data.get('expiry_date')
        img_src = data.get('img_src')

        if not data or not pcat or not pname or not pprice or not pstock: 
            return jsonify({"code": 400, "message": "Invalid data"}), 400
        
        new_product = Products(
            pcat=data['pcat'], 
            pname=data['pname'], 
            pdesc=data['pdesc'],
            img_src=data['img_src'],
            pprice=data['pprice'],
            stock=data['stock'],
            prod_date=data['prod_date'],
            expiry_date=data['expiry_date'])
    
        db.session.add(new_product)
        db.session.commit()

        return jsonify({"code": 201, "product_created": pname}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/update_product', methods=['PUT'])
def update_product():
    try:
        data = request.get_json()
        pid = data.get('pid')
        pcat = data.get('pcat')
        pname = data.get('pname')
        pprice = data.get('pprice')
        pstock = data.get('stock')

        pdesc = data.get('pdesc')
        img_src = data.get('img_src')
        prod_date = data.get('prod_date')
        expiry_date = data.get('expiry_date')
        
        if not data or not pid or not pcat or not pname or not pprice or not pstock:
            return jsonify({"code": 400, "message": "Invalid data"}), 400
        
        product = Products.query.filter_by(pid=pid).first()
        if not product:
            return jsonify({ "code": 404, "message": "Product not found"}), 404

        setattr(product, 'pcat', pcat)
        setattr(product, 'pname', pname)
        setattr(product, 'pprice', pprice)
        setattr(product, 'stock', pstock)
        setattr(product, 'pdesc', pdesc)
        setattr(product, 'img_src', img_src)
        setattr(product, 'prod_date', prod_date)
        setattr(product, 'expiry_date', expiry_date)

        db.session.commit()
        return jsonify({"code": 200, "message": "Product upated successfully."}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500        

@app.route('/delete_product', methods=['DELETE'])
def delete_product():
    try:
        data = request.get_json()
        pid = data.get('pid')
        
        if not data or not pid: 
            return jsonify({"code": 400, "message": "Invalid data"}), 400
        
        product = Products.query.filter_by(pid=pid).first()
        if product:
            db.session.delete(product)   
        
        db.session.commit()
        
        return jsonify({"code": 200, "message": f"product deleted successfully"}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ORDERS 
@app.route('/order_list', methods=['GET'])
def get_all_orders():
    try:
        orders = Orders.query.all()
        orders_list = []
        for order in orders:
            order_obj = {
                'oid': order.oid,
                'email': order.email,
                'pid': order.pid,
                'quantity': order.quantity,
                'status': order.status
            }

            orders_list.append(order_obj)
        
        return jsonify({"code": 200, "data": orders_list}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/create_order', methods=['POST'])
def create_order():
    try: 
        data = request.get_json()
        email = data.get('email')
        pid = data.get('pid')
        quantity = data.get('quantity')
        status = data.get('status')

        if not data or not email or not pid or not quantity: 
            return jsonify({"code": 400, "message": "Invalid data"}), 400
        
        new_order = Orders(
            email=email, 
            pid=pid, 
            quantity=quantity,
            status=status)
    
        db.session.add(new_order)
        db.session.commit()

        #retrieve orderID
        order = Orders.query.filter_by(email=email, pid=pid, quantity=quantity, status=status).order_by(Orders.oid.desc()).first()

        return jsonify({"code": 201, "order_id": f'{order.oid}'}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/update_order', methods=['PUT'])
def update_order():
    try:
        data = request.get_json()
        oid = data.get('oid')
        status = data.get('status')
        
        if not data or not oid or not status:
            return jsonify({"code": 400, "message": "Invalid data"}), 400
        
        order = Orders.query.filter_by(oid=oid).first()
        if not order:
            return jsonify({ "code": 404, "message": "Order not found"}), 404

        setattr(order, 'oid', oid)
        setattr(order, 'status', status)

        db.session.commit()
        return jsonify({"code": 200, "message": "Order updated successfully."}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500  


if __name__ == '__main__':
    app.run(debug=True, port=5000)