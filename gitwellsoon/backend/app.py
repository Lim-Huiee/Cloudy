from flask_cors import CORS
from classes import app
# from test import app
from features.products import products_bp
from features.accounts import accounts_bp
from features.orders import orders_bp

app.register_blueprint(products_bp)
app.register_blueprint(accounts_bp)
app.register_blueprint(orders_bp)

CORS(app)

@app.route('/', methods=["GET"])
def health_check():
    return "ok"

if __name__ == '__main__':
    app.run(debug=True, port=5000)