"""
***************************************************
Title: API practice
Author: Brogan Avery
Created: 2020-010-16
Description :
OS: macOS Catalina
Copyright : This is my own original work based on specifications issued by the course instructor
***************************************************
"""

import requests
import json
#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':

    response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=USD&apikey=ZZWP0X5B45GW57AC")
    response1 = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=ZZWP0X5B45GW57AC")
    response2 = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=DKK&apikey=ZZWP0X5B45GW57AC")

    pythoned_json = json.loads(response.text)
    pythoned_json1 = json.loads(response1.text)
    pythoned_json2 = json.loads(response2.text)

    exchangeRates = []

    exchangeRates.append(pythoned_json["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    exchangeRates.append(pythoned_json1["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    exchangeRates.append(pythoned_json2["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

    print('Exchange rates to US dollar :')
    print('Euro:   $',float(exchangeRates[0]))
    print('Bitcoin:   $', float(exchangeRates[1]))
    print('Danish krone:   $', float(exchangeRates[2]))
