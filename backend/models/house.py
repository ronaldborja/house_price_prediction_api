class House: 
    # Constructor -> To create object w the features to predict with the model params: 
    def __init__(self, square_footage: float, num_bedrooms: int, num_bathrooms: int, year_built: int, lot_size: float, garage_size: int, 
                 neighborhood_quality: int): 
            self.square_footage = square_footage
            self.num_bedrooms = num_bedrooms
            self.num_bathrooms = num_bathrooms
            self.year_built = year_built
            self.lot_size = lot_size
            self.garage_size = garage_size 
            self.neighborhood_quality = neighborhood_quality