from flask import request, jsonify, Blueprint
from storage import data_dict

tax_post_blueprint = Blueprint("tax_post", __name__)


@tax_post_blueprint.route('/v1/add/tax', methods=['POST'])
def add_tax():
    data = request.get_json()
    reg_id = data.get('reg_id')
    tax_rate = data.get('tax_rate')
    if data_dict['reg_id'] == reg_id:
        return jsonify({'ERROR': 'Reg_id существует!'}), 400
    else:
        data_dict['reg_id'] = reg_id
        data_dict['tax_rate'] = tax_rate
        print(data_dict)
        return jsonify({'message': 'Данные добавлены успешно!'})


@tax_post_blueprint.route('/v1/update/tax', methods=['POST'])
def update_tax():
    data_3 = request.get_json()
    reg_id = data_3.get('reg_id')
    tax_rate = data_3.get('tax_rate')
    if data_dict['reg_id'] == reg_id:
        data_dict['tax_rate'] = tax_rate
    else:
        return jsonify({'ERROR': 'Такого reg_id нет в словаре'}), 400
    print(data_dict)
    return jsonify({'SUCCESS': 'Данные обновлены!'}), 200