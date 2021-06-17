from decouple import config

DATABASE_NAME = config("DATABASE_NAME")
ADMIN_EMAIL = config("ADMIN_EMAIL")
ADMIN_PASSWD = config("ADMIN_PASSWD")
SECRET_KEY = config("SECRET_KEY")
