import requests
import pandas as pd


historical_BTC = requests.get('https://ftx.com/api/markets/BTC-PERP/candles?resolution=86400').json()
historical_BTC = pd.DataFrame(historical_BTC['result'])
historical_BTC['Nombre'] = 'BTC-PERP'


historical_ETH = requests.get('https://ftx.com/api/markets/ETH-PERP/candles?resolution=86400').json()
historical_ETH = pd.DataFrame(historical_ETH['result'])
historical_ETH['Nombre'] = 'ETH-PERP'


historical_SOL = requests.get('https://ftx.com/api/markets/SOL-PERP/candles?resolution=86400').json()
historical_SOL = pd.DataFrame(historical_SOL['result'])
historical_SOL['Nombre'] = 'SOL-PERP'


historical_LINK = requests.get('https://ftx.com/api/markets/LINK-PERP/candles?resolution=86400').json()
historical_LINK = pd.DataFrame(historical_LINK['result'])
historical_LINK['Nombre'] = 'LINK-PERP'

historical_BNB = requests.get('https://ftx.com/api/markets/BNB-PERP/candles?resolution=86400').json()
historical_BNB = pd.DataFrame(historical_BNB['result'])
historical_BNB['Nombre'] = 'BNB-PERP'


historical_ETC = requests.get('https://ftx.com/api/markets/ETC-PERP/candles?resolution=86400').json()
historical_ETC = pd.DataFrame(historical_ETC['result'])
historical_ETC['Nombre'] = 'ETC-PERP'


historical_XRP = requests.get('https://ftx.com/api/markets/XRP-PERP/candles?resolution=86400').json()
historical_XRP = pd.DataFrame(historical_XRP['result'])
historical_XRP['Nombre'] = 'XRP-PERP'


historical_CHZ = requests.get('https://ftx.com/api/markets/CHZ-PERP/candles?resolution=86400').json()
historical_CHZ = pd.DataFrame(historical_CHZ['result'])
historical_CHZ['Nombre'] = 'CHZ-PERP'

historical_DOT = requests.get('https://ftx.com/api/markets/DOT-PERP/candles?resolution=86400').json()
historical_DOT = pd.DataFrame(historical_DOT['result'])
historical_DOT['Nombre'] = 'DOT-PERP'


historical_DOGE = requests.get('https://ftx.com/api/markets/DOGE-PERP/candles?resolution=86400').json()
historical_DOGE = pd.DataFrame(historical_DOGE['result'])
historical_DOGE['Nombre'] = 'DOGE-PERP'


df_final = pd.concat([historical_LINK, historical_BTC, historical_SOL, historical_ETH, historical_BNB, historical_ETC, historical_XRP, historical_CHZ, historical_DOT, historical_DOGE], axis=0)

df_final.to_csv('criptosFinal.csv')