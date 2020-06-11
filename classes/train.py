import string
import csv
import numpy as np
import matplotlib.pyplot as plt

class ModelsTrainer:
    # Basic formula for linear regression: Y = ax + b
    # Where:
    # Y is the value we expect
    # y, x are the values, this is what we know

    def __init__(self, FilePath: str):
        self.learning_rate = 0.1
        with open(FilePath, "r") as csv_file:
            self.csv_reader = csv.reader(csv_file, delimiter=',')
            self._parse_data()

    def _parse_data(self):
        self.mileage = []
        self.price = []
        for row in self.csv_reader:
            if not str.isdigit(row[0]) or not str.isdigit(row[1]):
                continue
            self.mileage.append(float(row[0]))
            self.price.append(float(row[1]))
        self.mileage = np.array(self.mileage)
        self.price = np.array(self.price)

    def calculate_linear_regression(self):
        x = self.mileage
        y = self.price
        denominator = dot(x, x) - mean(x) * sum(x)
        print(denominator)
        # denominator = dot(x, x) - (sum(x) * sum(x)) / len(x)
        denominator = x.dot(x) - x.mean() * x.sum()
        a = (x.dot(y) - y.mean() * x.sum()) / denominator
        b = (y.mean() * x.dot(x) - x.mean() * x.dot(y)) / denominator

    def dot(list: [], value) ->list:



    def show_visualisation(self):
        plt.scatter(self.mileage, self.price)
        plt.xlabel("km")
        plt.ylabel("price")
        plt.show()

