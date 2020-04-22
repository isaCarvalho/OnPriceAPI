from connect import query_statement, execute_statement
from validate import validate_field, messages
from controller import Controller

class ProductController (Controller):

    def insert(self, request):

        data = request.json

        name = data.get('name')
        quantity = data.get('quantity')
        unity = data.get('unity')
        category = data.get('category')
        stamp = data.get('stamp')
        price = data.get('price')
        id_store = data.get('id_store')
        id = validate_field(request.args, 'id')

        if (id == -1):
            statement = "INSERT INTO products (name, quantity, unity, category, stamp, price, id_store) VALUES ('{}', {:d}, '{}', '{}', '{}', '{}', {:d})".format(name, quantity, unity, category, stamp, price, id_store)
        else:
            statement = "UPDATE products SET name = '{}', quantity = {:d}, unity = '{}', category = '{}', stamp = '{}', price = '{}', id_store = {:d} WHERE id = {:d}".format(name, quantity, unity, category, stamp, price, id_store, id)

        execute_statement(statement)

        return 'Data changed!'

    def listByStores(self, request):
        id = validate_field(request.args, 'id')

        return query_statement('SELECT * FROM products WHERE id_store = {:d}'.format(id)) if id != -1 else messages['NO_ID']
