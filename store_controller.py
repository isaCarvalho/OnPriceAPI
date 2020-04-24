from connect import query_statement, execute_statement
from validate import validate_field, messages
from controller import Controller
from product_controller import ProductController

class StoreController (Controller):

    def insert(self, request):

        data = request.json

        name = data.get('name')
        password = data.get('password')
        cnpj = data.get('cnpj')
        street = data.get('street')
        bairro = data.get('bairro')
        number = data.get('number')
        city = data.get('city')
        uf = data.get('uf')
        time = data.get('time')
        id = validate_field(request.args, 'id')

        if (id == -1):
            statement = "INSERT INTO stores (name, password, cnpj, street, bairro, number, city, uf, time) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name, password, cnpj, street, bairro, number, city, uf, time)
        else:
            statement = "UPDATE stores SET name = '{}', password = '{}', cnpj = '{}', street = '{}', bairro = '{}', number = '{}', city = '{}', uf = '{}', time = '{}' WHERE id = {:d}".format(name, password, cnpj, street, bairro, number, city, uf, time, id)

        execute_statement(statement)

        return 'Data changed!'

    def login(self, request):

        name = request.args.get('name')
        name = name.replace("%", " ")

        password = request.args.get('password')

        statement = "SELECT * FROM stores WHERE name = '{}' AND password = '{}'".format(name, password)

        store = None
        if (len(data) != 0):
            store = {
                "id": data[0][0],
                "name": data[0][1],
                "password": data[0][2],
                "cnpj": data[0][3],
                "street": data[0][4],
                "bairro": data[0][5],
                "number": data[0][6],
                "city": data[0][7],
                "uf": data[0][8],
                "time": data[0][9]
            }

        return store

    def listStores(self, request):
        data = Controller().list(request, "stores")
        array = []

        for (i in range(0, len(data), 1)):
            store = {
                "id": data[0][0],
                "name": data[0][1],
                "password": data[0][2],
                "cnpj": data[0][3],
                "street": data[0][4],
                "bairro": data[0][5],
                "number": data[0][6],
                "city": data[0][7],
                "uf": data[0][8],
                "time": data[0][9]
            }

            array.append(store)

        return array
