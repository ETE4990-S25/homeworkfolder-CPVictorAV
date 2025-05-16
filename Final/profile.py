
import requests
import xmltodict
import json
import random
from datetime import datetime, timedelta
import threading

rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]

def fetch_rates(c_date,base, output=False):
    """Fetching the XML Data"""
    if output:
        print("Current active threads: " + str(threading.active_count()))

    # base_choice = random.choice(ratesForBase)

    date_str = c_date.strftime("%Y-%m-%d")
    url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={date_str}&base_currency_code={base}&format_type=xml"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data_dict = xmltodict.parse(response.text)
        json_data = json.dumps(data_dict, indent=4)

        with open(f"{date_str}_exchange_rates_{base}.json", "a") as json_file:
            json_file.write(json_data)
    except Exception as e:
        print(f"Error fetching data for {date_str} with base {base}: {e}")

def threaded(debug=False):
    threads = []
    base_choice = random.choice(ratesForBase)
    s_date = datetime(2011, 5, 4)
    e_date = datetime(2025, 5, 16)
    inc_days = timedelta(days=365)

    while s_date <= e_date:
        thread = threading.Thread(target=fetch_rates, args=(s_date, base_choice, debug))
        thread.start()
        threads.append(thread)
        s_date += inc_days

    for thread in threads:
        thread.join()
def runIt(n): 
    for i in range(n): 
        threaded()

threaded(True)
