class PredictPrice:

    def __init__(self, theta0: int, theta1: int):
        self.theta0 = theta0
        self.theta1 = theta1
        self.price = 0

    def predict_price_by_mileage(self, mileage: int):
        self.price = self.theta0 + (self.theta1 * mileage)

    def get_price(self) -> float:
        return self.price
