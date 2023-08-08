import streamlit as st
import plotly.express as px
import functions

# web app features
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


# dynamic data plot
d, t = functions.get_data(days)
figure = px.line(x=d, y=t, labels={"x": "Date", "y":"Temperature (Celsius)"})
st.plotly_chart(figure)