# what_to_watch/opinions_app/api_views.py

from flask import jsonify

from . import app
from .models import Opinion

def opinion_to_dict(opinion):
    return dict(
        id = opinion.id,
        title = opinion.title,
        text = opinion.text,
        source = opinion.source,
        timestamp = opinion.timestamp,
        added_by = opinion.added_by
    )

@app.route('/api/opinions/<int:id>/', methods=['GET'])
def get_opinion(id):
    opinion = Opinion.query.get_or_404(id)
    # Конвертировать объект модели в словарь.
    data = opinion_to_dict(opinion)  
    return jsonify({'opinion': data}), 200