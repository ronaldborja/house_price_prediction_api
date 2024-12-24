from fastapi import HTTPException, status
from models.house import House
from models.regression import LinearReg
from schemes.house_scheme import HouseRequestModel
from schemes.price_prediction_schema import PricePredictionResponseModel
import json 
import numpy as np
from sqlalchemy.exc import SQLAlchemyError

class PricePredictionService: 

    @classmethod
    def predict(house: HouseRequestModel) ->  PricePredictionResponseModel:
        try:  
            # 1. Charge the model params to make preds: 
            model = LinearReg()
            W = model.load_weights()

            #2. Create the object House to get the params 
            new_house = House(**house.model_dump())

            #3. Cast to np array type
            new_house_array = np.array([
                new_house.square_footage, 
                new_house.num_bedrooms,
                new_house.num_bathrooms, 
                new_house.year_built, 
                new_house.lot_size, 
                new_house.garage_size, 
                new_house.neighborhood_quality
            ])

            new_house_array = new_house_array.reshape(1,-1)

            #3. Normalize the inputs
            new_house_normalized = model.normalize_features(new_house_array)

            #4. Make preds: 
            pred_arr = model.predict(W, new_house_normalized) 
            pred = float(pred_arr[0])
            return PricePredictionResponseModel(predicted_price=pred)
        
        except SQLAlchemyError as e: 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="There was a problem with the request")
