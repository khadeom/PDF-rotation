from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from rotatePdf import rotate

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pdfdatabase.db'
db = SQLAlchemy(app)


class PDFModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	outputPath = db.Column(db.String(100), nullable=False)
	angleOfRotation = db.Column(db.Integer, nullable=False)
	number = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"pdf(name = {outputPath}, angleOfRotation = {angleOfRotation}, number = {number})"


db.drop_all()
db.create_all()

pdf_post_args = reqparse.RequestParser()
pdf_post_args.add_argument("filePath", type=str, help="filePath of the pdf is required", required=True)
pdf_post_args.add_argument("angleOfRotation", type=int, help="angleOfRotation of the pdf", required=True)
pdf_post_args.add_argument("number", type=int, help="number on the pdf", required=True)

resource_fields = {
	'id': fields.Integer,
	'outputPath': fields.String,
	'angleOfRotation': fields.Integer,
	'number': fields.Integer
}

from rotatePdf import rotate


class RotatePdf(Resource):

	@marshal_with(resource_fields)
	def get(self, pdf_id):

		result = PDFModel.query.filter_by(id=pdf_id).first()
		if not result:
			abort(404, message="Could not find pdf with that id")

		return result

	@marshal_with(resource_fields)
	def post(self, pdf_id):

		args = pdf_post_args.parse_args()
		result = PDFModel.query.filter_by(id=pdf_id).first()
		if result:
			abort(409, message="PDF id taken...")

		outputPath = rotate(args['filePath'], args['angleOfRotation'],args['number'])

		pdf = PDFModel(id=pdf_id, outputPath=outputPath, angleOfRotation=args['angleOfRotation'], number=args['number'])
		db.session.add(pdf)
		db.session.commit()
		return pdf


api.add_resource(RotatePdf, "/pdf/<int:pdf_id>")

if __name__ == "__main__":
	app.run(debug=True)






