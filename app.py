from flask import Flask
from flask_cors import CORS
from models import db
from routes import routes, get_db_data

app = Flask(__name__)
CORS(app)
CORS(app, resources={r'/api/*': {'origins': '*'}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///humidity_database.db'
db.init_app(app)

app.register_blueprint(routes)

if __name__ == '__main__':
    with app.app_context():
        get_db_data()
    app.run(port=8000, debug=True)
