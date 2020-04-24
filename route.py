import flask
from flask import request, jsonify
from store_controller import StoreController
from product_controller import ProductController


app = flask.Flask(__name__)
app.config["DEBUG"] = True

baseUrlStores = 'stores'
baseUrlProducts = 'products'

@app.route('/', methods = ['GET'])
def home():
    return 'This is OnPriceApp API'

# Login
@app.route('/login', methods = ['GET'])
def login():
    return jsonify(StoreController().login(request))

# Returns a store by id or a list of all the stores in the system
@app.route('/' + baseUrlStores, methods = ['GET'])
def getStores():
    return jsonify(StoreController().listStores(request))

# Inserts a store in the database
@app.route('/' + baseUrlStores, methods = ['POST'])
def insertStore():
    return StoreController().insert(request)


# Modify a store in the database
@app.route('/' + baseUrlStores, methods = ['PUT'])
def putStore():
    return StoreController().insert(request)

# Deletes a store
@app.route('/' + baseUrlStores, methods = ['DELETE'])
def deleteStore():
    return StoreController().delete(request, 'stores')


# Return a products by it's id or all products
@app.route('/' + baseUrlProducts, methods = ['GET'])
def getProducts():
    return jsonify(ProductController().listProducts(request))

# Insert a product
@app.route('/' + baseUrlProducts, methods = ['POST'])
def insertProduct():
    return ProductController().insert(request)

# Modifies a product
@app.route('/' + baseUrlProducts, methods = ['PUT'])
def putProducts():
    return ProductController().insert(request)

# Deletes a product
@app.route('/' + baseUrlProducts, methods = ['DELETE'])
def deleteProduct():
    return ProductController().delete(request, 'products')

# Returns the products of a store
@app.route('/' + baseUrlStores + '/' + baseUrlProducts, methods = ['GET'])
def getStoresProducts():
    return jsonify(ProductController().listByStores(request))

@app.errorhandler(404)
def page_not_found(e):
    return 'This page was not found', 404
