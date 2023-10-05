import psycopg2


# psycopg2
# hiberbee theme


# connection = psycopg2.connect(
#     database="json_15_00", # название базы данных
#     password="123456",  # пароль
#     host="localhost",  # ссылка до базы данных, если она локальна, то localhost
#     user="postgres"  # владелец базы данных
# )
#
# cursor = connection.cursor()


class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            database="json_15_00",  # название базы данных
            password="123456",  # пароль
            host="localhost",  # ссылка до базы данных, если она локальна, то localhost
            user="postgres"  # владелец базы данных
        )

    def manager(self, sql, *args,
                commit=False,
                fetchone=False,
                fetchall=False):
        with self.connection as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    result = db.commit()
                if fetchone:
                    result = cursor.fetchone()
                if fetchall:
                    result = cursor.fetchall()
                return result


class TableCreator(Database):
    def create_categories_table(self):
        sql = """
            DROP TABLE IF EXISTS categories;
            CREATE TABLE IF NOT EXISTS categories(
                category_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
                category_name VARCHAR(100)            
            );
        """
        self.manager(sql, commit=True)

    def create_products_table(self):
        sql = """
            DROP TABLE IF EXISTS products;
            CREATE TABLE IF NOT EXISTS products(
                product_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
                title VARCHAR(200),
                description TEXT,
                price FLOAT,
                image TEXT,
                rate FLOAT,
                rate_count INTEGER,
                category_id INTEGER REFERENCES categories(category_id)
            );
        """
        self.manager(sql, commit=True)


class Manager(Database):
    def insert_categories(self, categories_list):
        sql = "INSERT INTO categories(category_name) VALUES (%s);"
        for category in categories_list:
            self.manager(sql, category, commit=True)
            print(f'new category {category}')

    def get_category_id_by_name(self, category_name):
        pass

    def insert_products(self, **kwargs):
        pass



# creator = TableCreator()
# creator.create_categories_table()
# creator.create_products_table()
