from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

data = []
class Shopvision(Resource):
    def post(self, newdata):
        occupant = {'occupancy': str(newdata)}
        data.append(occupant)
        return newdata

    def get(self):
        return {'data': data}

api.add_resource(Shopvision, '/')

@app.route("/")
def hello():
    return "Shop Vision API"
