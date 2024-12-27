from fastapi import APIRouter, Depends, HTTPException, status
from schemes.house_scheme import HouseRequestModel
from services.house_service import PricePredictionService

house_router = APIRouter(
    prefix='/houses',
    tags=["houses"],
)

@house_router.post("/predict", status_code=status.HTTP_201_CREATED)
async def predict_price(house: HouseRequestModel, service: PricePredictionService = Depends()): 
    try:
        price = service.predict(house) 
        return price
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Prediction failed: {str(e)}"
        )