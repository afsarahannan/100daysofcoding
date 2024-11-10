from cgi import print_arguments

import requests
from datetime import datetime, timedelta

from Quizzler.data import parameter

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":"WM654FE2B2LPBIQO"
}
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
key = 'Time Series (Daily)'
yesterday = (datetime.now()-timedelta(1)).strftime("%Y-%m-%d")
yesterday_closing = data[key][yesterday]['4. close']
closing_dict = {date: details['4. close'] for date, details in data[key].items()}
closing = [details['4. close'] for details in data[key].values()]

# print(f"{closing},\n{closing_dict},\n{yesterday_closing}")

# {'Meta Data': {'1. Information': 'Daily Prices (open, high, low, close) and Volumes', '2. Symbol': 'TSLA', '3. Last Refreshed': '2024-11-05', '4. Output Size': 'Compact', '5. Time Zone': 'US/Eastern'},
#  'Time Series (Daily)':
#      {'2024-11-05':{'1. open': '247.3400', '2. high': '255.2799', '3. low': '246.2101', '4. close': '251.4400', '5. volume': '65852493'},
#      '2024-11-04': {'1. open': '244.5600', '2. high': '248.9000', '3. low': '238.8800', '4. close': '242.8400', '5. volume': '68802354'},
#      '2024-11-01': {'1. open': '252.0430', '2. high': '254.0000', '3. low': '246.6300', '4. close': '248.9800', '5. volume': '57544757'}}

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday = (datetime.now()-timedelta(2)).strftime("%Y-%m-%d")
day_before_yesterday_closing = data[key][day_before_yesterday]['4. close']
print(day_before_yesterday_closing)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
# yesterday_closing = float(yesterday_closing)
# day_before_yesterday_closing = float(day_before_yesterday_closing)
#
diff = round(abs(yesterday_closing - day_before_yesterday_closing),2)
print(diff)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
# percentage_diff = round((diff/day_before_yesterday_closing)*100,2)
#
sign = ''
if yesterday_closing-day_before_yesterday_closing < 0:
    sign = '-'
    print(f"The day before yesterday' closing price decreased by {sign}{percentage_diff} moving from {day_before_yesterday_closing} to {yesterday_closing}")
else:
    sign = '+'
    print(f"The day before yesterday' closing price increased by {sign}{percentage_diff} moving from {day_before_yesterday_closing} to {yesterday_closing}")

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# news_parameters = {
#  "q":"Tesla",
#  "from":"2024-11-05",
#  "sortBy":"popularity",
#  "apiKey":"ade32a0c7e7548ac8874c9936e51d5e3"
# }

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


new_response = requests.get(url = "https://newsapi.org/v2/everything", params=news_parameters)
new_response.raise_for_status()
news = new_response.json()
print(news)

top_news = []

for n in range(3):
 article = news['articles'][n]['description']
 headline = news['articles'][n]['title']
 top_news.append(article)

print(top_news)
print(datetime.today().strftime('%Y-%m-%d'))


#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

message = []
for headline, article in zip(headline, article):
    message.append(f'Headline: {headline}. \nBrief:{article}')

#TODO 9. - Send each article as a separate message via Twilio. 
## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

