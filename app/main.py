from fastapi import FastAPI				
from app.api import tmf620_product_catalog				
from app.api import tmf622_product_order
from app.api import anomaly

app = FastAPI(title="TMF620 Product Catalog API")	
app.include_router(anomaly.router, prefix="/ai")			
				
app.include_router(				
    tmf620_product_catalog.router,				
    prefix="/tmf-api/productCatalog/v4"				
)				

app.include_router(
    tmf622_product_order.router,
    prefix="/tmf-api/productOrder/v4"
)
