import requests

def get_data():
    products =  requests.get("https://api.escuelajs.co/api/v1/products").json()

    for product in products:
        print(product['title'])