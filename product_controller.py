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

    def createArrayProducts(self, data):
        array = []

        for i in range(0, len(data), 1):
            product = {
                "id": data[i][0],
                "name": data[i][1],
                "qt": data[i][4],
                "unity": data[i][5],
                "category": data[i][2],
                "stamp": data[i][6],
                "price": data[i][3],
                "id_store": data[i][7]
            }

            array.append(product)

        return array


    def listProducts(self, request):
        data = Controller().list(request, "products")

        return self.createArrayProducts(data)


    def listByStores(self, request):
        id = validate_field(request.args, 'id')

        data = query_statement('SELECT * FROM products WHERE id_store = {:d}'.format(id))

        return self.createArrayProducts(data)
