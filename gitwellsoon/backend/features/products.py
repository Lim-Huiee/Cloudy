from flask import Blueprint, jsonify, request
from classes import db, Products

products_bp = Blueprint('products_bp', __name__)

@products_bp.route('/product_list', methods=['GET'])
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