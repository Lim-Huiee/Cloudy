from flask_cors import CORS
from test import app
from features.products import products_bp

app.register_blueprint(products_bp)

CORS(app)

@app.route('/', methods=["GET"])
def health_check():
    return "ok"

if __name__ == '__main__':
    app.run(debug=True, port=5000)