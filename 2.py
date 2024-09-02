import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
connection = None
try:
    connection = psycopg2.connect(user="postgres",
                                password="postgres",
                                host="127.0.0.1",
                                port="5432", 
                                options="-c client_encoding=UTF8"
                                )

    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()
    sql_create_database = 'create database postgres_db'
    cursor.execute(sql_create_database)
except (Exception, Error) as error:
    print("ошибка при работае с postSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("соединение с postgreSQL закрыто")
