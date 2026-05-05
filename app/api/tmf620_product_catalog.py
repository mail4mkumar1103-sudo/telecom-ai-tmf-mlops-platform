from fastapi import APIRouter, HTTPException	
from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: str
    name: str
    lifecycleStatus: str
    version: str
    price: Optional[float] = None

	
router = APIRouter()	
	
PRODUCTS = [	
    {"id": "DATA_10GB", "name": "10GB Pack", "lifecycleStatus": "Active", "version": "1.0", "price": 199},	
    {"id": "DATA_50GB", "name": "50GB Pack", "lifecycleStatus": "Draft", "version": "1.0", "price": 499},
    {"id": "VOICE_100", "name": "100 Min Pack", "lifecycleStatus": "Active", "version": "1.0", "price": 99},
    {"id": "VOICE_50", "name": "50 Min Pack", "lifecycleStatus": "Draft", "version": "1.0", "price": 49}	
]	
	
@router.get("/productOffering")
def get_products(
    lifecycleStatus: Optional[str] = None,
    name: Optional[str] = None
):
    results = PRODUCTS

    if lifecycleStatus:
        results = [p for p in results if p["lifecycleStatus"] == lifecycleStatus]

    if name:
        results = [p for p in results if name.lower() in p["name"].lower()]

    return {
        "status": "success",
        "data": results
    }

@router.get("/productOffering/{product_id}")
def get_product_by_id(product_id: str):
    for product in PRODUCTS:
        if product["id"] == product_id:
            if product["lifecycleStatus"] != "Active":
                raise HTTPException(status_code=404, detail= {"status": "error", "error": {"code": 400,"message": "Product not active"}})
           # return product
            return {"status": "success", "data": {"id": product["id"], "name": product["name"], "lifecycleStatus": product["lifecycleStatus"], "version": product["version"], "price": product["price"]}}
    raise HTTPException(status_code=404, detail= {"status": "error", "error": {"code": 404,"message": "Product not found" }})
    


@router.put("/productOffering/{product_id}")
def update_product(product_id: str, updated_product: Product):
    for product in PRODUCTS:
        if product["id"] == product_id:
            product.update(updated_product.dict())
           # return product
            return {"status": "success", "data": {"id": product["id"], "name": product["name"], "price": product["price"]}}
    raise HTTPException(status_code=404, detail= {"status": "error", "error": {"code": 404,"message": "Product not found" }})


@router.delete("/productOffering/{product_id}")
def delete_product(product_id: str):
    for product in PRODUCTS:
        if product["id"] == product_id:
            PRODUCTS.remove(product)
        #    return {"message": "Product deleted"}
            return {"status": "success", "data": {"message": "Product deleted"}
}
    raise HTTPException(status_code=404, detail= {"status": "error", "error": {"code": 404,"message": "Product not found" }})  


@router.post("/productOffering")
def create_product(product: Product):
    PRODUCTS.append(product.dict())
    return product