import requests

def get_symbols():
    response = requests.get("https://api.bybit.com/v2/public/symbols")
    response.raise_for_status()
    data = response.json()
    usdt_symbols = [symbol for symbol in data["result"] if symbol["quote_currency"] == "USDT"]
    return usdt_symbols

def get_ticker_info(symbol_name):
    response = requests.get(f"https://api.bybit.com/v2/public/tickers?symbol={symbol_name}")
    response.raise_for_status()
    return response.json()["result"][0]

def min_order_value(current_price, min_order_size):
    return current_price * min_order_size

def save_to_file(usdt_symbols):
    warning_coins = []

    with open("bybit_min_order_sizes.txt", "w") as file:
        file.write("Coin, Current Price, Min Order Size, Min Order Value, Warning\n")
        for symbol in usdt_symbols:
            ticker_info = get_ticker_info(symbol["name"])
            current_price = float(ticker_info["last_price"])
            min_order_size = float(symbol["lot_size_filter"]["min_trading_qty"])
            min_order_value_result = min_order_value(current_price, min_order_size)
            warning = "WARNING" if min_order_value_result > 0.05 else ""
            line = f'{symbol["base_currency"]}, {current_price}, {min_order_size}, {min_order_value_result:.6f}, {warning}\n'
            file.write(line)
            file.flush()  # Ensures the contents are flushed to disk after every write operation
            print(line.strip())  # Print the progress to the console

            if warning:
                warning_coins.append(symbol["name"])

    return warning_coins

def save_warning_coins(warning_coins):
    with open("warning_coins.txt", "w") as file:
        file.write(', '.join(warning_coins))

def main():
    usdt_symbols = get_symbols()
    warning_coins = save_to_file(usdt_symbols)
    save_warning_coins(warning_coins)

if __name__ == "__main__":
    main()
