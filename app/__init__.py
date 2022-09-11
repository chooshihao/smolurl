import configparser
from flask import Flask
from .models import db
from .shortener_bp import shortener_bp

def loadConfig(configFilename):
	config = configparser.ConfigParser()
	config.read(configFilename)

	return config

def init_app(testing=False):
	app = Flask(__name__)
	print(app.root_path)

	if testing:
		app.testing = True
		config = loadConfig("tests/test.conf")
	else:
		config = loadConfig("app/app.conf")

	app.config["SQLALCHEMY_DATABASE_URI"] = config["default"]["db_uri"]
	app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

	db.init_app(app)
	app.config["DATABASE"] = db

	app.register_blueprint(shortener_bp)

	app.run(debug=bool(config["default"]["debug"])
			, host=config["default"]["host"]
			, port=int(config["default"]["port"]))

	return app