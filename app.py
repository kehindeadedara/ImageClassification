from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
import random
import numpy as np

def random():
    randomlist = []
    for i in range(0, 10):
        n = np.random.randint(1, 30)
        randomlist.append(n)
    return randomlist

data = [50,10,20,30,40]
class Shopvision(Resource):

    def put(self, newdata):
        # newdata = {'name': newdata}
        # data.append(newdata)
        return newdata

    def get(self):
        return {'data': random()}

api.add_resource(Shopvision, '/')

@app.route("/")
def hello():
    return "Shop Vision API"


if __name__ == "__main__":
    app.run(debug= True);
