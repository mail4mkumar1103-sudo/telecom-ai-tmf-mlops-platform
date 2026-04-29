from fastapi import APIRouter
import random

router = APIRouter()

@router.post("/check")
def check_anomaly(data: dict):
    score = random.choice(["NORMAL", "ANOMALY"])
    return {"result": score}
