from fastapi import APIRouter	
	
router = APIRouter()	
	
PRODUCTS = [	
    {"id": "DATA_10GB", "name": "10GB Pack", "price": 199},	
    {"id": "DATA_50GB", "name": "50GB Pack", "price": 499},
    {"id": "VOICE_100", "name": "100 Min Pack", "price": 99}	
]	
	
@router.get("/productOffering")	
def get_products():	
    return PRODUCTS	
