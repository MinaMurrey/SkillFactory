import requests
import json
from config import keys

class APIException (Exception):
    pass

class CryptoConvertor:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote==base:
            raise APIException(f'Невозможо перевести одинаковые валюты {base}')

        try:
            quote_ticker= keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker=keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException (f'Не удалось обработать количество {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = amount* json.loads(r.content)[keys[base]]
        return total_base