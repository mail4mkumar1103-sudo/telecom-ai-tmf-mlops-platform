from fastapi import APIRouter, HTTPException	
from pydantic import BaseModel


class Product(BaseModel):
    id: str
    name: str
    price: int
	
router = APIRouter()	
	
PRODUCTS = [	
    {"id": "DATA_10GB", "name": "10GB Pack", "price": 199},	
    {"id": "DATA_50GB", "name": "50GB Pack", "price": 499},
    {"id": "VOICE_100", "name": "100 Min Pack", "price": 99}	
]	
	
@router.get("/productOffering")	
def get_products():	
    return PRODUCTS	

@router.get("/productOffering/{product_id}")
def get_product_by_id(product_id: str):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@router.put("/productOffering/{product_id}")
def update_product(product_id: str, updated_product: Product):
    for product in PRODUCTS:
        if product["id"] == product_id:
            product.update(updated_product.dict())
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/productOffering/{product_id}")
def delete_product(product_id: str):
    for product in PRODUCTS:
        if product["id"] == product_id:
            PRODUCTS.remove(product)
            return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")    


@router.post("/productOffering")
def create_product(product: Product):
    PRODUCTS.append(product.dict())
    return product