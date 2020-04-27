from validate import validate_field, messages
from connect import query_statement, execute_statement

class Controller:

    def list(self, request, table):
        id = validate_field(request.args)

        return query_statement('SELECT * FROM {} WHERE id = {:d}'.format(table, id)) if id != -1 else query_statement('SELECT * FROM {}'.format(table))

    def delete(self, request, table):
        id = validate_field(request.args, 'id')

        if id == -1:
            return messages['NO_ID']

        execute_statement('DELETE FROM {} WHERE id = {:d}'.format(table, id))

        return 'Data changed!'
