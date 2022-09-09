from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ShortURL(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	original_url = db.Column(db.String(2048), nullable=False)	
	url_id = db.Column(db.String(10))