import requests
from pprint import pprint


class RequestManager:
    base_url = "https://fakestoreapi.com"

    def get(self, endpoint):
        url = self.base_url + endpoint
        response = requests.get(url)
        return response.json()


# manager = RequestManager()
# categories = manager.get("/products/categories")
# products = manager.get("/products")
# # print(categories)
# pprint(products)


