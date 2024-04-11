import requests

import os
from dotenv import load_dotenv

load_dotenv()

RARIBLE_API_KEY = os.getenv("RARIBLE_API_KEY")

RARIBLE_API_URL="https://api.rarible.org/v0.1/data/collections/POLYGON:0x0ad52bfd0ddd09f581f0f790fe4f7369e9097712/floorPrice/?currency=MATIC"

def get():
    headers = {"X-API-KEY": RARIBLE_API_KEY}
    response = requests.get(RARIBLE_API_URL, headers=headers)
    data = response.json()

    previous = data["historicalValues"][-2]
    change_percent = round((abs(data["currentValue"] - previous) / previous) * 100.0, 2)

    if data["currentValue"] > previous:
        bot_message = (
            f"📈 Актуальный флор: {data['currentValue']} MATIC (+{change_percent}%)"
        )
        bot_speach = (
            f"Актуальный флор: {data['currentValue']} MATIC. На {change_percent}% больше, чем вчера."
        )
    elif data["currentValue"] == previous:
        bot_message = f"📊 Актуальный флор: {data['currentValue']} MATIC)"
        bot_speach = (
            f"Актуальный флор: {data['currentValue']} MATIC."
        )
    else:
        bot_message = (
            f"📉 Актуальный флор: {data['currentValue']} MATIC (-{change_percent}%)"
        )
        bot_speach = (
            f"Актуальный флор: {data['currentValue']} MATIC. На {change_percent}% меньше, чем вчера."
        )

    bot_message += f"\n\nВчера: {data['historicalValues'][-2]} MATIC"
    bot_message += f"\nПозавчера: {data['historicalValues'][-3]} MATIC"
    bot_speach += f"\n\nВчера: {data['historicalValues'][-2]} MATIC"
    bot_speach += f"\nПозавчера: {data['historicalValues'][-3]} MATIC"

    return bot_message, bot_speach

if __name__ == "__main__":
    print(get())