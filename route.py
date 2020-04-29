import flask
from flask_cors import CORS
from flask import request, jsonify
from store_controller import StoreController
from product_controller import ProductController


app = flask.Flask(__name__)
app.config["DEBUG"] = True

CORS(app, "resources = {r"/*": {"origins": "*"}})

baseUrlStores = 'stores'
baseUrlProducts = 'products'

@app.route('/', methods = ['GET'])
def home():
    return jsonify('This is OnPriceApp API'), 200

# Login
@app.route('/login', methods = ['GET'])
def login():
    return jsonify(StoreController().login(request)), 200

# Returns a store by id or a list of all the stores in the system
@app.route('/' + baseUrlStores, methods = ['GET'])
def getStores():
    return jsonify(StoreController().listStores(request)), 200

# Inserts a store in the database
@app.route('/' + baseUrlStores, methods = ['POST'])
def insertStore():
    return jsonify(StoreController().insert(request)), 200


# Modify a store in the database
@app.route('/' + baseUrlStores, methods = ['PUT'])
def putStore():
    return jsonify(StoreController().insert(request)), 200

# Deletes a store
@app.route('/' + baseUrlStores, methods = ['DELETE'])
def deleteStore():
    return jsonify(StoreController().delete(request, 'stores')), 200


# Return a products by it's id or all products
@app.route('/' + baseUrlProducts, methods = ['GET'])
def getProducts():
    return jsonify(ProductController().listProducts(request)),200

# Insert a product
@app.route('/' + baseUrlProducts, methods = ['POST'])
def insertProduct():
    return jsonify(ProductController().insert(request)), 200

# Modifies a product
@app.route('/' + baseUrlProducts, methods = ['PUT'])
def putProducts():
    return jsonify(ProductController().insert(request)), 200

# Deletes a product
@app.route('/' + baseUrlProducts, methods = ['DELETE'])
def deleteProduct():
    return jsonify(ProductController().delete(request, 'products')), 200

# Returns the products of a store
@app.route('/' + baseUrlStores + '/' + baseUrlProducts, methods = ['GET'])
def getStoresProducts():
    return jsonify(ProductController().listByStores(request)), 200

@app.errorhandler(404)
def page_not_found(e):
    return jsonify('This page was not found'), 404
