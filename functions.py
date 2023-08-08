import requests

API_KEY = "50a62aff2e129eb5d365687a1c7256c7"

# below is a function for pulling data from the api and filtering it based on the place
def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]   # filter data by forecast days

    return filtered_data


