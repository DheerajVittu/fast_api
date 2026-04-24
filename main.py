from fastapi import FastAPI

from models import Product

from database import session,engine

import database_models

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to"

products = [
    Product(id=1,quantity=10,price=99.9,description="Apple Phone",name="Iphone 17 Pro"),
    Product(id=2,quantity=10,price=99.9,description="Apple Phone",name="Iphone 17 Pro")
]

@app.get("/products")
def get_products():
    db = session()
    db.query()
    return products


@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product 
        
    return "Product Not Found"


@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product


@app.put("/product")
def update_product(id: int, product : Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product 
            return "Product Updated Successfully"
        
    return "product not found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted"
    return "Product Not Found"