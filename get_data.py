import config, csv
from binance.client import Client
client = Client(config.API_SECRET, config.API_SECRET)

# get all symbol prices
# prices = client.get_all_tickers()

# for price in prices:
#     print(price)

# print(len(prices))

candles = client.get_klines(symbol='BTCBUSD', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('2021.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

# for candlestick in candles:
#     print(candlestick)
#     candlestick_writer.writerow(candlestick)

# print(len(candles))

# fetch 5 minute klines for the last day up until now
candlesticks = client.get_historical_klines("BTCBUSD", Client.KLINE_INTERVAL_5MINUTE, "1 Dec, 2020", "1 Jan, 2021")

for candlestick in candlesticks:
    candlestick_writer.writerow(candlestick)

csvfile.close()