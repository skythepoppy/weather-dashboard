import streamlit as st
import plotly.express as px
from functions import get_data

# web app features ( title, text input, slider, select box)
st.title("Weather Dashboard")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1,
                 max_value=5,
                 help="Select the number of days in which you'd like to observe the city's forecast.")
option = st.selectbox("Select the data you'd like to view",
                      ("Temperature", "Sky"))   # creates a dropdown menu with the options Temp and Sky


# subheader display prior to data plot
if days == 1 and option == "Sky":
    st.subheader(f"Below is the forecast for tomorrow in {place}")
elif days == 1 and option == "Temperature":
    st.subheader(f"Below is the {option} for tomorrow in {place}")
else:
    st.subheader(f"Below is the {option} for the next {days} days in {place}")

if place:
    # get weather data
    filtered_data = get_data(place, days)

    # dynamic data plot
    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]  # filter temp data via temp dict key
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y":"Temperature (Celsius)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear":"images/clear.png",
                  "Clouds":"images/cloud.png",
                  "Rain":"images/rain.png",
                  "Snow":"images/snow.png",}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]  # filter sky data via weather dict key
        image_path = [images[condition] for condition in sky_conditions]    # access image value from key
        st.image(image_path, width=110)

