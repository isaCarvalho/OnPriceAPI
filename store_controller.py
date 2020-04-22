from connect import query_statement, execute_statement
from validate import validate_field

class StoreController:

    def list(self, request):
        id = validate_field(request.args)

        return query_statement('SELECT * FROM stores WHERE id = {:d}'.format(id)) if id != -1 else query_statement('SELECT * FROM stores')


    def insert(self, request):

        name = validate_field(request.args, 'name')
        password = validate_field(request.args, 'password')
        cnpj = validate_field(request.args, 'cnpj')
        street = validate_field(request.args, 'street')
        bairro = validate_field(request.args, 'bairro')
        number = validate_field(request.args, 'number')
        city = validate_field(request.args, 'city')
        uf = validate_field(request.args, 'uf')
        time = validate_field(request.args, 'time')
        id = validate_field(request.args, 'id')

        if (id != -1):
            statement = 'INSERT INTO stores (name, password, cnpj, street, bairro, number, city, uf, time) VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {})'.format(name, password, cnpj, street, bairro, number, city, uf, time)
        else:
            statement = 'UPDATE stores SET name = {} AND password = {} AND cnpj = {} AND street = {} AND = bairro = {} AND number = {} AND city = {} AND uf = {} AND time = {} WHERE id = {:d}'.format(name, password, cnpj, street, bairro, number, city, uf, time, id)

        execute_statement(statement)

        return 'Data changed!'

    def delete(self, request):
        id = validate_field(request.args, 'id')

        return execute_statement('DELETE FROM stores WHERE id = {:d}'.format(id)) if id != -1 else messages['NO_ID']
