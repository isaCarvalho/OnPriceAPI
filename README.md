# On Price API REST

This is the Python Flask API for OnPriceApp.
[OnPriceAPI](https://onpriceapi.herokuapp.com)

# Endpoints:

* / [GET] <br/>
This is home.

* /stores [GET|POST] <br/>
Returns an array with all the stores in the system.

* /stores?id={id} [GET|PUT|DELETE] <br/>
Returns a specific store

* /products [GET|POST] <br/>
Returns an array the products in the system.

* /product?id={id} [GET|PUT|DELETE] <br/>
Returns a specific product

* /stores/products?id={id} [GET] <br/>
Returns an array with a store's products.

# Requisites

- Python3
- PostgreSQL 11

Run the packages.sh file to install all the packages to modify this API

# Author

* Isabela Carvalho
* All the contributors

# Observations

Make sure you install all the pip packages. To deploy this package, It was created
a virtual enviroment. Do not forget to install gunicorn and make the `Procfile`
if you want to deploy.
