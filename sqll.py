import mysql.connector
from mysql.connector import Error

try:
    with mysql.connector.connect(
        host='localhost',
        user='root',
        password='root'
    ) as connection:

        if connection.is_connected():
            print("подключение к mysql установлено.")

            with connection.cursor() as cursor:

                cursor.execute("CREATE DATABASE IF NOT EXISTS MyfirstDB")
                print("база данныx MyfirstDB создана")
                
                cursor.execute("USE MyfirstDB")

                cursor.execute("""
                create table if not exists Employees (
                    id int AUTO_increment Primary key,
                    name varchar(255) not null,
                    position varchar(255) not null,
                    salary decimal(10,2) not null
                )
                """)
                print("таблица создана")


                insert_query = """
                INSERT INTO Salary(name,position,salary)
                VALUES (%s,%s,%s)
                
                
                """
                records = [
                    ('Alice','Manager', 70000),
                    ('Bob','Developer',60000),
                    ('Charlie','Analist',50000)

                ]
                cursor.executemany(insert_query,records)
                connection.commit()
                print(f"Вставлено {cursor.rowcount} записей в таблицу Salary")

                cursor.execute("SELECT * FROM Salary")
                rows = cursor.fetchall()
                print("данные из таблицы Salary:")
                for row in rows:
                    print(row)

except Error as e:
    print(f"ошибка при подключении к MySQL: {e}")

print("соединение с MySQL закрыто.")

