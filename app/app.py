from flask import Flask, request, Response, jsonify
from models.ShortURL import ShortURL, db
from hashids import Hashids
import configparser
import os

def main():
	config = configparser.ConfigParser()
	config.read(os.path.dirname(os.path.realpath(__file__)) + "/app.conf")
	config.sections()

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

	app.add_url_rule("/", "helloworld", hello_world, methods=["GET"])
	app.add_url_rule("/app/create", "createurl", createURL, methods=["POST"])

	app.run(debug=True, host=config["default"]["host"], port=int(config["default"]["port"]))

def hello_world():
	return "<p>hello world</p>"

def generateURLID(val: int, min_length:int=6, salt:str="testing"):
	hid = Hashids(salt=salt, min_length=min_length)
	return hid.encode(val)

def createURL():
	json_data = request.get_json(force=True)
	original_url = json_data["original_url"]

	shorturl_entry = ShortURL(original_url=original_url)

	db.session.add(shorturl_entry)
	db.session.flush()
	shorturl_entry.url_id = generateURLID(shorturl_entry.id)
	db.session.commit()

	return jsonify({"status": "success", "short_url_id": shorturl_entry.url_id})

if __name__ == "__main__":
	main()