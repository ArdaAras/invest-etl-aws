import infrastructure as infra
import yfinance as yf
from utils import nasdaq_stocks_dict, column_names
from datetime import datetime, timedelta

def get_stocks_history() -> None:
    # compose file name (yesterday's date)
    fileName = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d') + ".csv"
    
    # write header
    with open(fileName, "a") as myfile:
        myfile.write(column_names + "\n")

    # write actual data
    for stock in nasdaq_stocks_dict:
        currentTicker = yf.Ticker(stock)
        hist = currentTicker.history(period="1d")
        data_list = hist.values.tolist()
        with open(fileName, "a") as myfile:
            line = f"{stock},"
            for itemlist in data_list:
                for item in itemlist:
                    line += str(item) + ","
                line = line.rstrip(',')
                line += "\n"
            myfile.write(line)
        
    pass

def main():
    #infra.create_cloudwatch_rule()
    
    # Get yesterday's history of all stocks
    #get_stocks_history()

    pass

if __name__ == "__main__":
    main()
