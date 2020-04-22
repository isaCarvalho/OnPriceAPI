import psycopg2
from config import config

def query_statement(statement = 'SELECT version()'):
    conn = None
    data = None

    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(statement)

        data = cur.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

        return data

def execute_statement(statement = 'SELECT version()'):
    conn = None
    data = None

    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        cur.execute(statement)
        cur.statusmessage

        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
