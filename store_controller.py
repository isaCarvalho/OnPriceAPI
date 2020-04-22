from connect import query_statement, execute_statement
from validate import validate_field, messages
from controller import Controller
from product_controller import ProductController

class StoreController (Controller):

    def insert(self, request):

        name = request.form.get('name')
        password = request.form.get('password')
        cnpj = request.form.get('cnpj')
        street = request.form.get('street')
        bairro = request.form.get('bairro')
        number = request.form.get('number')
        city = request.form.get('city')
        uf = request.form.get('uf')
        time = request.form.get('time')
        id = validate_field(request.args, 'id')

        if (id == -1):
            statement = "INSERT INTO stores (name, password, cnpj, street, bairro, number, city, uf, time) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name, password, cnpj, street, bairro, number, city, uf, time)
        else:
            statement = "UPDATE stores SET name = '{}' AND password = '{}' AND cnpj = '{}' AND street = '{}' AND bairro = '{}' AND number = '{}' AND city = '{}' AND uf = '{}' AND time = '{}' WHERE id = {:d}".format(name, password, cnpj, street, bairro, number, city, uf, time, id)

        execute_statement(statement)

        return 'Data changed!'

    def deleteStore(self, request):
        if (ProductController().listByStores(request) != []):
            return 'This store contains products, so it cannot be deleted!', 403

        return super.delete(request, 'stores')
