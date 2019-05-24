import quandl
import pandas as pd
import os


def scrapper():

    quandl.ApiConfig.api_key = '4_ERbyf3sSDTz8qsDsoM'
    symbol = "ICICIBANK"
    DIR = os.getcwd()
    nifty=pd.read_csv(DIR+"/Historicaldata/ind_nifty50list.csv")
    error=[]

    for ele,symbol in enumerate(list(nifty["Symbol"])):
        for i in range(2010,2019):
            print("Stock: ",ele," Year No: ",i)
            try:
                data=quandl.get('NSE/'+symbol,start_date=str(i)+'-01-01', end_date=str(i)+'-12-31')
                if not (os.path.exists(DIR+"/Historicaldata/" +str(i))):
                    os.mkdir(DIR+"/Historicaldata/" +str(i))
                data.to_csv(DIR+"/Historicaldata/%s/%s-%s.csv" % (i, symbol, i))
            except:
                print("Not Found")
                error.append(ele)

if __name__ == '__main__':
    scrapper()