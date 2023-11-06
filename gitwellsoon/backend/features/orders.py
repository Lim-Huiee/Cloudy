from flask import Blueprint, jsonify, request
from classes import db, Orders

orders_bp = Blueprint('orders_bp', __name__)

@orders_bp.route('/order_list', methods=['GET'])
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
    
@orders_bp.route('/create_order', methods=['POST'])
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

@orders_bp.route('/update_order', methods=['PUT'])
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
        return jsonify({"code": 200, "message": "Order upated successfully."}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500     