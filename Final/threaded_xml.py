from datetime import datetime, timedelta #needed for incrementing time (i learned from help())
import threading #threaded process

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