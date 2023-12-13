from flask import request, jsonify, Blueprint
from storage import data_dict

tax_fetch_blueprint = Blueprint("tax_fetch", __name__)


@tax_fetch_blueprint.route('/v1/fetch/taxes', methods=['GET'])
def fetch_taxes():
    return jsonify(data_dict)


@tax_fetch_blueprint.route('/v1/fetch/tax', methods=['GET'])
def fetch_tax():
    data_1 = request.get_json()
    reg_id = data_1.get('reg_id')
    if data_dict['reg_id'] == reg_id:
        return data_dict
    else:
        return ({'ERROR': 'Такого reg_id нет в словаре'}), 400


@tax_fetch_blueprint.route('/v1/fetch/calc', methods=['GET'])
def fetch_calc():
    data_2 = request.get_json()
    reg_id = data_2.get('reg_id')
    price = data_2.get('price')
    mounth = data_2.get('mounth')
    if data_dict['reg_id'] != reg_id:
        return jsonify({'ERROR': 'Такого reg_id нет в словаре'}), 400
    else:
        tax = data_dict['tax_rate'] * price * mounth / 12
        return jsonify({'Налог за год': tax})
