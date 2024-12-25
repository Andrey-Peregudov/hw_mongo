import json

from flask import Flask, Response
from pymongo import MongoClient
from bson import json_util

from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__, static_folder='static', template_folder='templates')
client = MongoClient('mongo', 27017)
db = client['flask_mongodb']
collection = db['users']


@app.route('/add/<name>/<age>')
def add(name=None, age=18):
    result = collection.insert_one({'name': name, 'age': age})

    otv = JSONEncoder().encode(result.inserted_id)
    return {'j': otv}


@app.route('/all')  # список всех элементов коллекции
def all():
    result = collection.find()
    return json_util.dumps(result)


@app.route('/find_all/<name>')  # поиск всех элементов в коллекции по ключу
def find_all(name=None):
    result = collection.find({'name': name})
    return json_util.dumps(result)


@app.route('/find_one/<name>')  # поиск одного элемента в коллекции по ключу
def find_one(name=None):
    result = collection.find_one({'name': name})
    return json_util.dumps(result)


@app.route('/dell/<name>')  # Удаление одного элемента
def dell(name=None):
    result = collection.delete_one({'name': name})
    return json_util.dumps(result)


@app.route('/update/<age>/<new_name>')
def update(age, new_name):
    result = collection.update_one({'age': age}, {'$set': {'name': new_name}})
    return json_util.dumps(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
