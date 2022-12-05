class UserService:
    def login(self, user_name, password):
        if not user_name:
            raise Exception("Invalid user name.")
        elif not password:
            raise Exception("Invalid password.")


    def register(self, user_name, password):
        pass
