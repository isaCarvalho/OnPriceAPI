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
