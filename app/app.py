import configparser
import os
from flask import Flask
from models import db
from shortener_bp import shortener_bp

def loadConfig():
	config = configparser.ConfigParser()
	config.read(os.path.dirname(os.path.realpath(__file__)) + "/app.conf")
	print(config.sections())

	return config

def init_app():
	config = loadConfig()

	app = Flask(__name__)
	app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://%s:%s@%s:%s/%s" % (
												config["database"]["username"],
												config["database"]["password"],
												config["database"]["host"],
												config["database"]["port"],
												config["database"]["database"],
											)
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

	db.init_app(app)
	app.register_blueprint(shortener_bp)

	app.run(debug=True, host=config["default"]["host"], port=int(config["default"]["port"]))

	return app

if __name__ == "__main__":
	init_app()