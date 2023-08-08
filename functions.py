import requests


API_KEY = "50a62aff2e129eb5d365687a1c7256c7"


'''
def get_data(days):
    dates = ["2022-35-10", "2022-26-09", "2022-23-08"]
    temperature = [10,15,9]
    temperatures = [days * i for i in temperature]
    return dates, temperatures
'''
def get_data(place, forecast_days, kind):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]   # filter data by forecast days

    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]    # filter temp data via temp dict key
    elif kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]  # filter sky data (via weather dict key)

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind='Temperature'))