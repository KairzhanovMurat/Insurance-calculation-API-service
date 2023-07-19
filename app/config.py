from decouple import config

DB_NAME = config('DB_NAME')
DB_PASS = config('DB_PASS')
DB_HOST = config('DB_HOST')
DB_USER = config('DB_USER')

db_url = f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
