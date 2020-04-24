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

    def listProducts(self, request):
        data = Controller().list(request, "products")

        return createArrayProducts(data)


    def listByStores(self, request):
        id = validate_field(request.args, 'id')

        data = query_statement('SELECT * FROM products WHERE id_store = {:d}'.format(id))

        return createArrayProducts(data)

    def createArrayProducts(data):
        array = []

        for i in range(0, len(data), 1):
            product = {
                "id": data[0][0],
                "name": data[0][1],
                "qt": data[0][2],
                "unity": data[0][3],
                "category": data[0][4],
                "stamp": data[0][5],
                "price": data[0][6],
                "id_store": data[0][7]
            }

            array.append(product)

        return array
