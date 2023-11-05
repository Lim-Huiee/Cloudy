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

        if not data or not email or not pid or not quantity: 
            return jsonify({"code": 400, "message": "Invalid data"}), 400
        
        new_order = Orders(
            email=email, 
            pid=pid, 
            quantity=quantity)
    
        db.session.add(new_order)
        db.session.commit()

        return jsonify({"code": 201, "order_created": "Successfully created orders"}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@orders_bp.route('/update_order', methods=['POST'])
def update_order():
    pass

# @appointment_bp.route('/update_appointment', methods=['PUT'])
# def update_appointment():
#     try:
#         data = request.get_json()
#         school = data.get('school')
#         old_appointment = data.get('oldAppointment')
#         new_appointment = data.get('newAppointment')
#         new_rank_group = data.get('newRankGroup')
        
#         if not data or not school or not old_appointment or not new_appointment:
#             return jsonify({"code": 400, "message": "Invalid data"}), 400
        
#         appointment_name = Appointment.query.filter_by(school_name=school, appointment_name=old_appointment).first()
#         if not appointment_name:
#             return jsonify({ "code": 404, "message": "Appointment name not found"}), 404

#         setattr(appointment_name, 'rank_group', new_rank_group)
#         setattr(appointment_name, 'appointment_name', new_appointment)

#         ClinicianSchoolAppointments = ClinicianSchoolAppointment.query.filter_by(school_name=school, appointment_name=old_appointment).all()
#         for each in ClinicianSchoolAppointments:
#             setattr(each, 'appointment_name', new_appointment)

#         db.session.commit()
#         return jsonify({"code": 200, "message": f"Appointment name updated successfully from {old_appointment} to {new_appointment}"}), 200


#     except Exception as e:
#         return jsonify({'error': str(e)}), 500        
