from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    humidity = db.Column(db.Integer, nullable=False)
    time = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Data: {self.id}>'
