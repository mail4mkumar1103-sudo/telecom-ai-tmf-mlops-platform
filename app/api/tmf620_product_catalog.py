from fastapi import APIRouter	
	
router = APIRouter()	
	
PRODUCTS = [	
    {"id": "DATA_10GB", "name": "10GB Pack", "price": 199},	
    {"id": "VOICE_100", "name": "100 Min Pack", "price": 99}	
]	
	
@router.get("/productOffering")	
def get_products():	
    return PRODUCTS	
