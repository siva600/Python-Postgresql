from user import User

# my_user = User("siva.vattikutti99@gmail.com", "Siva", "Vattikutti", None)

my_user = User("gerry.smith@gmail.com", "smith", "henry", None)

user_from_db_email = User.load_from_db_by_email("siva.vattikutti99@gmail.com")


my_user.save_to_db()
print(user_from_db_email)
