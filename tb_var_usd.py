import requests
import time
import datetime
import os
last_update_id = 0
cur_list = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN',
            'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL',
            'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY',
            'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 'EGP',
            'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 'GHS',
            'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF',
            'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD',
            'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT',
            'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD',
            'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN',
            'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK',
            'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR',
            'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD',
            'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY',
            'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VES',
            'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR',
            'ZMW', 'ZWL']

token = os.environ['TBOT_TOKEN']
# token = token_1
while True:
    result = requests.get(
        f'https://api.telegram.org/{token}/getUpdates',
        params={'offset': last_update_id + 1})
    data = result.json()
    for update in data['result']:
        last_update_id = update['update_id']
        chat_id = update['message']['chat']['id']
        mes = update['message']['text']
        message = mes.upper()
        print(message)
        if message in cur_list:

            r = requests.get(f'https://open.er-api.com/v6/latest/{mes}')

            # нет необходимости импортировать модуль json отдельно,
            # все нужное есть в модуле requests
            d = r.json()
            currency = (d["rates"]['RUB'])

        elif message == "ВАЛЮТА":
            currency = ', '.join(cur_list)

        else:
            currency = "Введите валюту или посмотрите список набрав: 'Валюта'"

        send_result = requests.get(
            f'https://api.telegram.org/{token}/sendMessage',
            params={'chat_id': chat_id, 'text': currency})
