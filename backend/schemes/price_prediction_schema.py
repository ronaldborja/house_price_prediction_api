from pydantic import BaseModel, ConfigDict

class PricePredictionRequestModel(BaseModel):
    predicted_price: float 
    model_config: ConfigDict = {
    }

class PricePredictionResponseModel(BaseModel): 
    predicted_price: float 
    model_config = ConfigDict(from_attributes=True)