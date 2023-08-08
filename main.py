import streamlit as st

st.title("Weather Dashboard")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1,
                 max_value=5,
                 help="Select the number of days in which you'd like to observe the city's forecast.")
option = st.selectbox("Select the data you'd like to view",
                      ("Temperature", "Sky"))   # creates a dropdown menu with the options Temp and Sky
if days == 1 and option == "Sky":
    st.subheader(f"Here is the forecast for tomorrow in {place}")
elif days == 1 and option == "Temperature":
    st.subheader(f"Here is the {option} for tomorrow in {place}")
elif option == "Sky":
    st.subheader(f"Here is the forecast for the next {days} days in {place}")
elif option == "Temperature":
    st.subheader(f"Here is the Temperature for the next {days} days in {place}")