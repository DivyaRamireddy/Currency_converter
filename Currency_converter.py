def currency_converter():
    print("Welcome to Currency Converter 💱")

    # Fixed conversion rates (example values)
    rates = {
        "USD": 0.012,   # 1 INR = 0.012 USD
        "EUR": 0.011,   # 1 INR = 0.011 EUR
        "JPY": 1.8      # 1 INR = 1.8 JPY
    }

    amount = float(input("Enter amount in INR: "))
    print("Available currencies:", ", ".join(rates.keys()))
    choice = input("Convert to: ").upper()

    if choice in rates:
        converted = amount * rates[choice]
        print(f"{amount} INR = {converted:.2f} {choice}")
    else:
        print("Invalid currency choice ❌")


currency_converter()
