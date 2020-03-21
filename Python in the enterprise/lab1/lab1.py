import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.datasets as sk
from sklearn.linear_model import LinearRegression as reg


def function():
    boston_lib = sk.load_boston()
    boston_dataFrame = pd.DataFrame(boston_lib.data, columns=boston_lib.feature_names)
    pd.options.display.max_columns = None
    print(boston_dataFrame.head())

    chosen_two = ["CRIM", "DIS"]
    pd.DataFrame.hist(boston_dataFrame, chosen_two, color='k')
    plt.show()

    a = np.array(boston_lib.target)  # creating array of target(price) elemets

    for i in chosen_two:
        b = np.array(boston_dataFrame[i])  # creating a copy of array
        plt.scatter(b, a, marker='o', color='k', label='Actual data')  # scattering
        b = b.reshape(-1, 1)  # reshaping our copy of array to make LinearRegression possible
        tmp = reg().fit(b, a.reshape(-1, 1))  # used LinearRegression as reg()
        pred = tmp.predict(b)  # predicted values

        # Plot stuff

        plt.xlabel(i)
        plt.ylabel('TARGET(PRICE)')
        plt.grid()
        plt.plot(b, pred, 'r-', label='Prediction')
        plt.legend(loc='upper right')

        plt.show()


def main(args):
    function()


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
