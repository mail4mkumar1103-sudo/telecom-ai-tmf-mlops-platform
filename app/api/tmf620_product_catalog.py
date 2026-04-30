from fastapi import APIRouter, HTTPException	
	
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

