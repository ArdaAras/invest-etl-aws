# Complete stock market data pipeline with AWS

PART-1

1) Pull yesterday's NASDAQ stock data from https://finance.yahoo.com/
2) Write raw data to S3\
&nbsp;&nbsp; - This bucket shall be created with [**boto3**](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
4) Trigger this event daily with AWS Lambda and CloudWatch\
&nbsp;&nbsp; - After NASDAQ normal trading session which is between 9:30 AM - 4:00 PM

PART-2

TBD

## Technologies and Tools

**yfinance API** (https://github.com/ranaroussi/yfinance), AWS S3, Lambda, CloudWatch

## Files
    1. dl.cfg           : Contains access, secret access keys and redshift database configuration information.
    2. config.cfg       : Contains keys, bucket name and region information to be used within the project.
    3. requirements.txt : Contains libraries used.
    4. 2023-09-22.csv   : Sample NASDAQ stock data fetched on 22 Sept 2023.

## Author

[Arda Aras](https://www.linkedin.com/in/arda-aras/)
