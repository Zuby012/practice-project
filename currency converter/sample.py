# Simple Currency Converter

# Exchange rates (example: 1 USD to others)
rates = {
    'USD': 1.0,
    'EUR': 0.92,
    'GBP': 0.78,
    'JPY': 158.5,
    'INR': 83.5,
    'NGN': 1528.52
}


def convert(amount, from_currency, to_currency):
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Unsupported currency.")
    usd_amount = amount / rates[from_currency]
    return usd_amount * rates[to_currency]


if __name__ == "__main__":
    print("Available currencies:", ', '.join(rates.keys()))
    from_curr = input("Convert from: ").upper()
    to_curr = input("Convert to: ").upper()
    amount = float(input("Amount: "))
    try:
        result = convert(amount, from_curr, to_curr)
        print(f"{amount} {from_curr} = {result:.2f} {to_curr}")
    except Exception as e:
        print("Error:", e)
