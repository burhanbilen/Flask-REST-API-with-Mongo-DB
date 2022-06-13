from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask import make_response
from bson.json_util import dumps
import yaml

app = Flask(__name__)

with open('db.yaml') as db_config_file:
    db_config = yaml.load(db_config_file, Loader = yaml.SafeLoader)

app.config['MONGO_URI'] = f"mongodb://{db_config['server']}:{db_config['port']}/{db_config['db_name']}"
mongo = PyMongo(app)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/', methods = ['GET'])
def Homepage():
    return jsonify({"Instruction":
    {"#1 | /Books": "Get all books",
     "#2 | /Books/<title>":"Get books by name",
     "#3 | /Author/<name>":"Get books by author name",
     "#4 | /Books":"Add new books with POST method and JSON Body",
     "#5 | /Books/<title>":"Update books with PUT method",
     "#6 | /Books/<title>":"Delete books by title"
     }})

@app.route('/Books', methods = ['GET'])
def Books():
    all_books = mongo.db.Books.find()
    return dumps(all_books)

@app.route('/Books/<string:title>', methods = ['GET'])
def getBook(title):
    wanted_books = list(mongo.db.Books.find({'title':title}))
    return dumps(wanted_books)

@app.route('/Author/<string:name>', methods = ['GET'])
def getAuthorBooks(name):
    author_books = list(mongo.db.Books.find({'author':name}))
    return dumps(author_books)

@app.route('/Books', methods = ['POST'])
def addBooks():
    if request.headers['Content-Type'] == "application/json":
        new_book = request.json
        try:
            mongo.db.Books.insert_many(new_book)
        except:
            return make_response(jsonify({'error': 'Not Added'}), 404)
        else:
            return make_response(jsonify({'info': 'Successfully Added'}), 200)

@app.route('/Books/<string:title>', methods = ['PUT'])
def updateBooks(title):
    if request.headers['Content-Type'] == "application/json":
        book_document = request.json
        try:
            mongo.db.Books.update_many({"title": title}, {"$set": book_document})
        except:
            return make_response(jsonify({'error': 'Not Updated'}), 404)
        else:
            return make_response(jsonify({'info': 'Successfully Updated'}), 200)

@app.route('/Books/<string:title>', methods = ['DELETE'])
def deleteBooks(title):
    try:
        mongo.db.Books.delete_many({"title":title})
    except:
        return make_response(jsonify({'error': 'Not Deleted'}), 404)
    else:
        return make_response(jsonify({'info': 'Successfully Deleted'}), 200)

if __name__ == "__main__":
    app.run(debug = True)