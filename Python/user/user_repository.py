import pymysql


class UserRepository:
    def __init__(self):
        self.db = pymysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="user",
            port=3306,
            charset='utf8mb4'
        )

    def find_by_name(self, user_name):
        print(user_name)
        return None

    def add_user(self, user):
        sql = "insert into user (id, name, passwd) values (1, user.user_name, user.password)"
        cursor = self.db.cursor()
        cursor.execute(sql)
