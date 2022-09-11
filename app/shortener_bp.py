from urllib import response
from flask import Blueprint, redirect, request, jsonify, render_template
from markupsafe import escape
from .models import ShortURL, db
from hashids import Hashids

shortener_bp = Blueprint("shortener_bp", __name__)

@shortener_bp.route("/", methods=["GET"], strict_slashes=True)
def renderHome():
	return render_template("index.html")

@shortener_bp.route("/<url_id>", methods=["GET"])
def resolveURL(url_id):
	if not url_id:
		return

	shorturl_entry = ShortURL.query.filter_by(url_id=url_id).first()
	# TODO: handle invalid id

	if shorturl_entry:
		return redirect(escape(shorturl_entry.original_url))
	else:
		return render_template("404.html"), 404

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