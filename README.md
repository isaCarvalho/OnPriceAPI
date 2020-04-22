# On Price API REST

This is the Python Flask API for OnPriceApp.

# Endpoints:

* / [GET]
This is home.

* /stores [GET]

You may pass the store id in the request if you want to return a specific store

* /stores?id={id} [PUT|POST|DELETE]

* /products [GET]

You may pass the product id if you want to return a specific product

* /product?id={id} [PUT|POST|DELETE]

* /stores/products?id={id}

Here you may pass the store id to list all the products of a specific store.
If you do not pass anything, it will return the products grouped by stores.

# Requisites

- Python3
- PostgreSQL 11

Run the packages.sh file to install all the packages to modify this API

# Author

* Isabela Carvalho
* All the contributors
