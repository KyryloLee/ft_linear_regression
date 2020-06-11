from classes.predict import PredictPrice
import ft_linear_regresion

def main():
    x = PredictPrice()
    x.predict_price_by_mileage(100)
    print(x.get_price())

if __name__ == "__main__":
    main()