import requests # from the take home
import xmltodict
import json




def fetch_rates(c_date,base, output=False):
    """Fetching the XML Data"""
    if output:
        print("Current active threads: " + str(threading.active_count())) # check if thread running

    
    # uses the current set date
    date_str = c_date.strftime("%Y-%m-%d")
    url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={date_str}&base_currency_code={base}&format_type=xml"

    # xml data extract
    try:
        response = requests.get(url)
        response.raise_for_status()
        data_dict = xmltodict.parse(response.text)
        json_data = json.dumps(data_dict, indent=4)

        with open(f"{date_str}_exchange_rates_{base}.json", "a") as json_file:
            json_file.write(json_data)
    except Exception as e:
        print(f"Error fetching data for {date_str} with base {base}: {e}")