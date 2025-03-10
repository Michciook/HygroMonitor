from flask import Blueprint, render_template, jsonify, request, redirect
from models import db, HData
import datetime

routes = Blueprint('routes', __name__)

values = [0] * 20
labels = [1] * 20

target_humidity = 0


def update_chart_data(humidity, timestamp):
    values.pop(0)
    values.append(humidity)
    labels.pop(0)
    labels.append(timestamp)


@routes.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        global target_humidity
        target_humidity = request.form['target_humidity']
        return redirect('/')
    else:
        return render_template('index.html')


@routes.route('/api/data/', methods=['GET'])
def get_data():
    try:
        return jsonify({'labels': list(labels), 'values': list(values)})
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@routes.route('/api/test/', methods=['GET'])
def test_data():
    try:
        rows = db.session.query(HData).order_by(HData.id.desc()).limit(50).all()
        data = [{'id': row.id, 'humidity': row.humidity, 'time': row.time} for row in rows]
        return jsonify(data, target_humidity)
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@routes.route('/api/get_readings/', methods=['POST'])
def get_readings():
    try:
        content = request.get_json()
        if not content or 'humidity' not in content:
            return jsonify({'error': 'Invalid JSON format'}), 400
        if content['humidity'] is None or not isinstance(content['humidity'], int) or not (0 <= content['humidity'] <= 100):
            return jsonify({'error': 'Invalid data'}), 400
        
        timestamp = datetime.datetime.now().strftime('%H:%M:%S')
        new_data = HData(humidity=content['humidity'], time=timestamp)

        db.session.add(new_data)
        db.session.commit()
        
        update_chart_data(content['humidity'], timestamp) 
        
        return jsonify({'message': 'Data received successfully'}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Server error: {str(e)}'}), 500


def get_db_data():
    latest_rows = db.session.query(HData).order_by(HData.id.desc()).limit(20).all()
    for row in latest_rows:
        values.pop()
        values.insert(0, row.humidity)
        labels.pop()
        labels.insert(0, row.time)
