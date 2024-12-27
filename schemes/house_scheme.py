from pydantic import BaseModel, ConfigDict

class HouseRequestModel(BaseModel):
    square_footage: float
    num_bedrooms: int
    num_bathrooms: int
    year_built: int
    lot_size: float 
    garage_size: int
    neighborhood_quality: int 


class HouseResponseModel(BaseModel): 
    square_footage: float
    num_bedrooms: int
    num_bathrooms: int
    year_built: int
    lot_size: float 
    garage_size: int
    neighborhood_quality: int 
    model_config = ConfigDict(from_attributes=True)