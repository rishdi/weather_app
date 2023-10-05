from api import RequestManager
from db import Manager


def main():
    request_manager = RequestManager()
    db_manager = Manager()

    categories = request_manager.get("/products/categories")
    db_manager.insert_categories(categories)
main()