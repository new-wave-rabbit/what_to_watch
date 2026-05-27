from flask import jsonify, request

from . import app, db
from .models import Opinion
from .views import random_opinion

@app.route('/api/opinions/<int:id>/', methods=['GET'])
def get_opinion(id):
    opinion = Opinion.query.get_or_404(id)
    return jsonify({'opinion': opinion.to_dict()}), 200

@app.route('/api/opinions/<int:id>/', methods=['PATCH'])
def update_opinion(id):
    data = request.json()
    opinion = Opinion.query.get_or_404(id)
    if Opinion.query.filter_by(text=data['text']).first is not None:
        return jsonify({'error': 'Такое мнение в базе уже есть'}), 400

    opinion.title = request.json.get('title', opinion.title)
    opinion.text = request.json.get('text', opinion.text)
    opinion.source = request.json.get('source', opinion.source)
    opinion.added_by = request.json.get('added_by', opinion.added_by)
    db.session.commit()  
    return jsonify({'opinion': opinion.to_dict()}), 201

@app.route('/api/opinions/<int:id>/', methods=['DELETE'])
def delete_opinion(id):
    opinion = Opinion.query.get_or_404(id)
    db.session.delete(opinion)
    db.session.commit()
    return '', 204


@app.route('/api/opinions/', methods=['GET'])
def get_opinions():
    opinions = Opinion.query.all()  
    opinions_list = [opinion.to_dict() for opinion in opinions]
    return jsonify({'opinions': opinions_list}), 200


@app.route('/api/opinions/', methods=['POST'])
def add_opinion():
    data = request.get_json(silent=True)
    reqired_fields = ['title', 'text']
    if data is None or set(reqired_fields) & set(data.keys()) != set(reqired_fields):
        return jsonify({'error': 'В запросе отсутствуют обязательные поля'}), 400
    
    if Opinion.query.filter_by(text=data['text']).first is not None:
        return jsonify({'error': 'Такое мнение в базе уже есть'}), 400

    opinion = Opinion()
    opinion.from_dict(data)
    db.session.add(opinion)
    db.session.commit()
    return jsonify({'opinion': opinion.to_dict()}), 201

@app.route('/api/get-random-opinion/', methods=['GET'])
def get_random_opinion():
    opinion = random_opinion()
    return jsonify({'opinion': opinion.to_dict()}), 200