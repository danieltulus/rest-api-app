from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)

api = Api(app)

CORS(app)

db = SQLAlchemy(app)

basedir = os.path.dirname(os.path.abspath(__file__))
database = "sqlite:///" + os.path.join(basedir, "db.sqlite")
app.config["SQLALCHEMY_BINDS"] = "sqlite://test.db"

class ModelDatabase(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nama = db.Column(db.String(100))
	umur = db.Column(db.Integer)
	alamat = db.Column(db.TEXT)

	def save(self):
		try:
			db.session.add(self)
			db.session.commit()
			return True
		except:
			return False

db.create_all()

identitas = {}

class ContohResource(Resource):
	def get(self):
		return identitas

	def post(self):
		dataNama = request.form["nama"]
		dataUmur = request.form["umur"]
		dataAlamat = request.form["alamat"]

		model = ModelDatabase(nama=dataNama, umur=dataUmur, alamat=dataAlamat)
		model.save()
		response = {
			"msg": "Data berhasil ditambahkan",
			"code": 200

		}
		return response, 200

api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
	app.run(debug=True, port=5005)