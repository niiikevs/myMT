import requests

def get_usdt_pairs():
    """Получает список всех фьючерсных пар к USDT с Binance."""
    url = "https://fapi.binance.com/fapi/v1/exchangeInfo"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pairs = []
        
        # Фильтруем пары с quoteAsset USDT
        for symbol_info in data['symbols']:
            if symbol_info['quoteAsset'] == 'USDT':
                pairs.append(symbol_info['symbol'])
        
        return pairs
    else:
        print(f"Ошибка: {response.status_code}")
        return []

def get_daily_volume(symbol):
    """Получает суточный объем торгов для заданной пары."""
    url = f"https://fapi.binance.com/fapi/v1/ticker/24hr?symbol={symbol}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Проверяем наличие ключа 'quoteVolume'
        if 'quoteVolume' in data:
            return float(data['quoteVolume'])  # Суточный объем в USDT
        else:
            print(f"Ключ 'quoteVolume' не найден для {symbol}.")
            return None
    else:
        print(f"Ошибка: {response.status_code} для {symbol}.")
        return None

def print_pairs_and_volumes(pairs):
    """Выводит пары и их суточный объем в терминал."""
    print(f"{'Пара':<10} {'Суточный объем (USDT)':<25}")
    print("=" * 35)
    
    for pair in pairs:
        volume = get_daily_volume(pair)
        if volume is not None:
            print(f"{pair:<10} {volume:<25,.2f}")  # Форматируем вывод

if __name__ == "__main__":  # Исправлено здесь
    usdt_pairs = get_usdt_pairs()
    print_pairs_and_volumes(usdt_pairs)
