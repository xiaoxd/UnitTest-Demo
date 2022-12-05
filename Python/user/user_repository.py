import mysql.connector


class UserRepository:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="user"
        )

    def find_by_name(self, user_name):
        return None

    def add_user(self, user):
        sql = "insert into user (id, name, passwd) values (1, user.user_name, user.password)"
        cursor = self.db.cursor()
        cursor.execute(sql)