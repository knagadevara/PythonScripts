from flask import Flask , jsonify , request
from flask_restful import Api , Resource

app = Flask(__name__)
api = Api(app)

