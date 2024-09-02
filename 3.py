import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user='postgres',
                                password = 'postgres',
                                host='1278.0.0.1',
                                port='5432',
                                database='postgres_db')
    
    cursor = connection.cursor()

    print('Информация о сенрвере PostgreSQL')
    print(connection.get_dsn_parameters(), "\n")

    cursor.execute("SELECT version();")

    resord = cursor.fetchone()
    print("Вы подключилины к - ", resord, "\n")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с  PostgreSQL закрыто")