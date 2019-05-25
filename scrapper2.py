import quandl
import pandas as pd
import os


def scrapper():

    quandl.ApiConfig.api_key = '4_ERbyf3sSDTz8qsDsoM'
    DIR = os.getcwd()
    nifty=pd.read_csv(DIR+"/Historicaldata/ind_nifty50list.csv")
    error=[]

    for ele,symbol in enumerate(list(nifty["Symbol"])):
            print("Stock: ",ele)
            try:
                data=quandl.get('NSE/'+symbol,start_date=str(2015)+'-01-01', end_date=str(2019)+'-12-31')
                if not (os.path.exists(DIR+"/Historicaldata/")):
                    os.mkdir(DIR+"/Historicaldata/")
                data.to_csv(DIR+"/Historicaldata/%s-2015-19.csv" % (symbol))
            except:
                print("Not Found")
                error.append([ele,symbol])
    print(error)

if __name__ == '__main__':
    scrapper()