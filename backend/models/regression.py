import numpy as np
import json

# Vectorized Linear Regression from Scratch: 
# Based on: https://gist.github.com/akashjaswal/d175d1ef5d45c9cc4662d3e82e20bc96

class LinearReg:
    # Constructor 
     
    # 1. Feature vector (m,n) + bias (m, 1) 
    # 2. Output (y) -> (m, 1)
    # 3. Weight matrix -> Zeros matrix (num_features, 1)
    # 4. Grad descent: 
        # predict -> error -> loss -> gradient -> new params -> repeat 

    def __init__(self, lr = 0.1, iterations = 1000, 
                 normalize = True, fit_intercept=True):
        
        self.iterations = iterations
        self.lr = lr 
        self.normalize = normalize 
        self.fit_intercept = fit_intercept

    # Normalize -> Values between -1 to 1 
    def normalize_features(self, X) -> np.ndarray:
        mean = np.array([
            2813.900000,
            2.968750,
            1.971250,
            1986.902500,
            2.772345,
            1.015000, 
            5.596250 
        ])


        std_dev = np.array([
            1251.986627, 
            1.420484,
            0.815735,
            20.796526,
            1.282339,
            0.819924,
            2.913458
        ])

        return (X - mean)/ std_dev

    
    # Adjust X vector based on the needs of the user 
    def prepare_features(self, X: np.ndarray) -> np.ndarray: 
        if self.normalize:
            X = self.normalize_features(X)

        if self.fit_intercept:
            bias = np.ones(shape=(len(X), 1))
            X = np.append(bias, X, axis=1) # we append the bias as the 1st col 

        return X 
    
    # Initialize weights as 0 
    def init_weights(self, num_features: int) -> np.ndarray: 
        return np.zeros((num_features,1))

    def predict(self, W, features): 
        return np.dot(features, W) # dot product 
    
    def compute_error(self, y, y_pred): 
        return (y - y_pred)
    
    def compute_loss(self, error, num_samples): 
        return (1.0/num_samples)*np.sum(error**2)
    
    # Derivative of J with respect to theta: 
    def compute_gradients(self, features, error, num_samples): 
        return (-2.0/num_samples)*np.dot(features.T, error)
    
    def update_weights(self, W, gradients): 
        return W - self.lr*gradients
    
    def fit(self, X, y):
        y = np.array(y)
        y = y.reshape(len(y), 1)
        features = self.prepare_features(X)
        num_samples, num_features = features.shape
        W = self.init_weights(num_features)

        for i in range(self.iterations):
            y_pred = self.predict(W, features)
            error = self.compute_error(y, y_pred)
            loss = self.compute_loss(error, num_samples)
            gradients = self.compute_gradients(features, error, num_samples)
            W = self.update_weights(W, gradients)

        return W
    
    def save_weights(self, W, filename="trained_weights.json"):
        weights_dict = {"weights": W.tolist()}
        with open(filename, "w") as f:
            json.dump(weights_dict, f)
        print(f"Weights saved to {filename}")

    def load_weights(self, filename="trained_weights.json"):
        with open(filename, "r") as f:
            loaded_weights_dict = json.load(f)
        return np.array(loaded_weights_dict["weights"])
