import configparser
import os
from flask import Flask
from models import db
from shortener_bp import shortener_bp

def loadConfig(configFilename):
	config = configparser.ConfigParser()
	config.read(os.path.join(os.path.dirname(os.path.realpath(__file__)), configFilename))

	return config

def init_app(testing=False):
	app = Flask(__name__)

	if testing:
		app.testing = True
		config = loadConfig("test.conf")
	else:
		config = loadConfig("app.conf")

	app.config["SQLALCHEMY_DATABASE_URI"] = config["default"]["db_uri"]
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

	db.init_app(app)
	app.register_blueprint(shortener_bp)

	app.run(debug=bool(config["default"]["debug"])
			, host=config["default"]["host"]
			, port=int(config["default"]["port"]))

	return app

if __name__ == "__main__":
	init_app()