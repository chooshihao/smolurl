from flask import Blueprint, redirect, request, jsonify
from markupsafe import escape
from .models import ShortURL, db
from hashids import Hashids

shortener_bp = Blueprint("shortener_bp", __name__)

@shortener_bp.route("/<url_id>", methods=["GET"])
def resolveURL(url_id):
	shorturl_entry = ShortURL.query.filter_by(url_id=url_id).first()
	# TODO: handle invalid id

	return redirect(escape(shorturl_entry.original_url))

def generateURLID(val: int, min_length:int=6, salt:str="testing"):
	hid = Hashids(salt=salt, min_length=min_length)
	return hid.encode(val)

@shortener_bp.route("/app/create", methods=["POST"])
def createURL():
	json_data = request.get_json(force=True)
	original_url = json_data["original_url"]

	# TODO: validate URL

	shorturl_entry = ShortURL(original_url=original_url)
	
	db.session.add(shorturl_entry)
	db.session.flush()
	shorturl_entry.url_id = generateURLID(shorturl_entry.id)
	db.session.commit()

	return jsonify({"status": "success", "short_url_id": shorturl_entry.url_id})