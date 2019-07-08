import pandas as pd
import numpy as np





class CCIAGent:
    def __init__(self, days=20):
        self.x = days

    def model(self, df):
        self.df = df
        df_cci = (df - df.rolling(self.x).mean()) / (0.015 * df.rolling(self.x).std())
        self.df_cci = df_cci

    def model_cci_history(self, start, end, initial=100000):
        crossing = []
        profit = 0
        i = start
        if (end > self.df.size):
            raise ValueError("Data not available for given range")
        while i < end:
            if (self.df_cci.iloc[i, 0] == "NaN"):
                i = i + 1
                continue
            if (self.df_cci.iloc[i, 0] >= 100):
                t0 = i
                shares = initial / self.df.iloc[i, 0]
                while (self.df_cci.iloc[i, 0] >= -100 and i < end):
                    i = i + 1
                profit += (self.df.iloc[i, 0] - self.df.iloc[t0, 0]) * shares
                i = i + 1
            else:
                i = i + 1
        print("Profit Earned in CCI: %s (%s%%)" % (profit, profit / initial * 100))
