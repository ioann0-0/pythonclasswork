import mysql.connector
from mysql.connector import Error

def create_user(username,password):
    try:
        cursor.execute(f"CREATE USER '(username)'@'localhost' IDENTIFIED BY '(password)'")
        cursor.execute(f"GRANT ALL PRIVILEGIES ON *.* TO '(username)'@'localhost'")
        cursor.execute("FLUSH PRIVILEGIES")
        print(f"Пользователь (username) создан и привилегии назначены.")
    except mysql.connector.Error as err:
        print(f"ОШИБКА ПРИ СОЗДАНИИ ПОЛЬЗОВАТЕЛЯ: {err:msg}")