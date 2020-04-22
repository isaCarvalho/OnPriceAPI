messages = {
    'NO_ID' : 'Error: There was no id provided. Please provide the id and try again'
}

def validate_field(array, field = 'id'):

    if field in array:
        return int(array.get('{}'.format(field)))
    else:
        return -1
