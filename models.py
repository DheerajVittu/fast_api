from pydantic import BaseModel

class Product(BaseModel) :
    id : int
    quantity: int
    price : float
    description : str
    name: str    