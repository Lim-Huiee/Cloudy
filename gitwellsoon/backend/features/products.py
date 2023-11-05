from flask import Blueprint, jsonify, request
from classes import db, Products
# from test import db, Products
from datetime import datetime

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
    
@products_bp.route('/create_product', methods=['POST'])
def create_product():
    try: 
        data = request.get_json()
        pcat = data.get('pcat')
        pname = data.get('pname')
        pprice = data.get('pprice')
        pstock = data.get('stock')

        
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

@products_bp.route('/update_product', methods=['PUT'])
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

@products_bp.route('/delete_product', methods=['DELETE'])
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
