from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Request Schema
class ProductOffering(BaseModel):
    id: str

class ProductOrderItem(BaseModel):
    action: str
    productOffering: ProductOffering

class ProductOrder(BaseModel):
    productOrderItem: List[ProductOrderItem]
    relatedParty: dict

ORDERS = []

@router.post("/productOrder")
def create_order(order: ProductOrder):
    order_dict = order.dict()
    order_dict["status"] = "PENDING"
    ORDERS.append(order_dict)
    return order_dict

@router.get("/productOrder")
def get_orders():
    return ORDERS
