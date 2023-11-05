from flask import Blueprint, jsonify, request
from classes import db, Products
# from test import db, Products

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
