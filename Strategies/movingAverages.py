import pandas as pd
import numpy as np




class SMA():
    def __init__(self, days=20):
        self.x = days

    def model(self, df):
        if not len(df.columns) == 1:
            raise ValueError("Number of Columns should be one")

        zero_data = np.zeros(shape=(df.size, 1))
        df_sma = pd.DataFrame(zero_data, columns=df.columns)

        for i in range(0, df_sma.size):
            if x == 1:
                ma = df.iloc[i, 0]
            if i < x - 1:
                ma = df.iloc[:i, 0].mean()
                df_sma.iloc[i, 0] = ma
            else:
                df_sma.iloc[i, 0] = ma
                try:
                    ma = ma - df.iloc[i - x + 1, 0] / x + df.iloc[i + 1, 0] / x
                except:
                    pass
            self.df_sma = df_sma

    def model_profit_history(self, df, start, end, initial=100000):
        crossing = []
        profit = 0
        i = start
        self.model(df)
        if (end > self.df_sma.size):
            raise ValueError("Data not available for given range")

        while i < end:
            if (self.df_sma.iloc[i, 0] < df.iloc[i, 0]):
                #         BuyIng Point
                t0 = i
                shares = initial / df.iloc[i, 0]
                while (self.df_sma.iloc[i, 0] < df.iloc[i, 0] and i < end):
                    i = i + 1
                profit += (df.iloc[i, 0] - df.iloc[t0, 0]) * shares
                crossing.append([t0, i])
                t0 = i
            i = i + 1

        if (df.iloc[i, 0] > df.iloc[t0, 0]):
            profit += (df.iloc[i, 0] - df.iloc[t0, 0]) * shares
            print(len(crossing))

            print("Profit Earned in sma: %s (%s%%)" % (profit, profit / initial * 100))


class EMA():
    def __init__(self, days=20, smoothing=2):
        self.x = days
        self.s = smoothing

    def model(self, df):
        if not len(df.columns) == 1:
            raise ValueError("Number of Columns should be one")

        zero_data = np.zeros(shape=(df.size, 1))
        df_ema = pd.DataFrame(zero_data, columns=df.columns)

        for i in range(0, df_ema.size):
            if self.x == 1:
                ema = df.iloc[i, 0]
            elif i < self.x - 1:
                ema = df.iloc[:i, 0].mean()
                df_ema.iloc[i, 0] = ema
            else:
                ema = df.iloc[i, 0] * self.s / (self.x + 1) + df_ema.iloc[i - 1, 0] * (1 - self.s / (self.x + 1))
                df_ema.iloc[i, 0] = ema
        self.df_ema = df_ema

    def model_profit_history(self, df, start, end, initial=100000):
        crossing = []
        profit = 0
        i = start
        self.model(df)
        if (end > self.df_ema.size):
            raise ValueError("Data not available for given range")

        while i < end:
            if (self.df_ema.iloc[i, 0] < df.iloc[i, 0]):
                #         BuyIng Point
                t0 = i
                shares = initial / df.iloc[i, 0]
                while (self.df_ema.iloc[i, 0] < df.iloc[i, 0] and i < end):
                    i = i + 1
                profit += (df.iloc[i, 0] - df.iloc[t0, 0]) * shares
                crossing.append([t0, i])
                t0 = i
            i = i + 1

        if (df.iloc[i, 0] > df.iloc[t0, 0]):
            profit += (df.iloc[i, 0] - df.iloc[t0, 0]) * shares
            print(len(crossing))

            print("Profit Earned in ema: %s (%s%%)" % (profit, profit / initial * 100))
