def read_float(message):
    value = None
    while value is None:
        value = input(message)
        try:
            value = int(value)
            return value
        except:
            try:
                value = float(value)
                return value
            except:
                print("Not int or float")
                value = None

    return value


def read_client_data(client_name):
    months = read_float(f"How many months for {client_name}? ")
    client_payments = []  # lista
    client_data = {
        "payments": [],
        "avg_payment": None,
        "next_payment": None,
    }

    for month in range(months):
        payment = read_float(f"Payment for month {month}: ")
        # float(input(f"Payment for month {month}: "))
        client_payments.append(payment)

    print(f"Payments for last year for client {client_name} are: {client_payments}")

    # our_clients[client_name] = client_payments
    client_data["payments"] = client_payments
    client_data["avg_payment"] = sum(client_payments) / months
    client_data["next_payment"] = client_data["avg_payment"] * 1.06

    return client_data
