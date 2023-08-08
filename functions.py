def get_data(days):
    dates = ["2022-35-10", "2022-26-09", "2022-23-08"]
    temperature = [10,15,9]
    temperatures = [days * i for i in temperature]
    return dates, temperatures