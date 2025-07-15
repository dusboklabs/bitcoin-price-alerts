import requests
import time

# Настройки
LOWER_LIMIT = 60000   # Минимальный порог
UPPER_LIMIT = 70000   # Максимальный порог
CHECK_INTERVAL = 60   # Проверка каждые N секунд

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd"}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()["bitcoin"]["usd"]
    except Exception as e:
        print(f"❌ Ошибка при получении цены: {e}")
        return None

def check_price():
    print("🔔 Bitcoin Price Alert запущен. Ожидание событий...\n")
    while True:
        price = get_btc_price()
        if price:
            print(f"📈 Текущая цена BTC: ${price:,.2f}")
            if price < LOWER_LIMIT:
                print(f"⚠️ Цена упала ниже ${LOWER_LIMIT:,.2f}!")
            elif price > UPPER_LIMIT:
                print(f"🚀 Цена превысила ${UPPER_LIMIT:,.2f}!")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    check_price()
