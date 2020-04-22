from connect import query_statement, execute_statement
from validate import validate_field, messages
from controller import Controller

class ProductController (Controller):

    def insert(self, request):

        name = validate_field(request.args, 'name')
        quantity = validate_field(request.args, 'quantity')
        unity = validate_field(request.args, 'unity')
        category = validate_field(request.args, 'category')
        stamp = validate_field(request.args, 'stamp')
        price = validate_field(request.args, 'price')
        id_store = validate_field(request.args, 'id_store')
        id = validate_field(request.args, 'id')

        if (id != -1):
            statement = 'INSERT INTO products (name, quantity, unity, category, stamp, price, id_store) VALUES ({}, {}, {}, {}, {}, {}, {:d})'.format(name, quantity, unity, category, stamp, price, id_store)
        else:
            statement = 'UPDATE products SET name = {} AND quantity = {} AND unity = {} AND category = {} AND stamp = {} AND price = {} AND id_store = {:d} WHERE id = {:d}'.format(name, quantity, unity, category, stamp, price, id_store, id)

        execute_statement(statement)

        return 'Data changed!'

    def listByStores(self, request):
        id = validate_field(request.args)

        return query_statement('SELECT * FROM products WHERE id_store = {:d}'.format(id)) if id != -1 else messages['NO_ID']
