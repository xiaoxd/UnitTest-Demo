import datetime


class User:
    user_name = ""
    password = ""
    disable = False
    expire = datetime.datetime.now().now()
