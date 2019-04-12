import psycopg2
from database import ConnectionFromPool


class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return "User {}".format(self.email)

        # connection
        # create cursor
        # ---execute or insert sql commands
        # commit connection
        # close connection

    def save_to_db(self):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute('insert into customers(email, first_name, last_name) values (%s, %s, %s)',
                               (self.email, self.first_name, self.last_name))

    @classmethod
    def load_from_db_by_email(cls, email):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute('select * from customers where email=%s', (email,))
                user_data = cursor.fetchone()
                return cls(email=user_data[1], last_name=user_data[2],first_name=user_data[3], id=user_data[0])

    @classmethod
    def load_from_db_by_name(cls, first_name):
        with ConnectionFromPool() as connection:
            with connection.cursor() as cursor:
                cursor.execute('select * from customers where first_name =%s', (first_name,))
                user_data = cursor.fetchall()
                return cls(email=user_data[1], first_name=user_data[2], last_name=user_data[3], id=user_data[0])




