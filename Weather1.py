import streamlit as st
import requests

# Function to fetch weather data
def get_weather(city):
    api_key = "aaf7299c07be1200796a877f4d8fc4ee"  # Updated API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    return response.json()

# Streamlit app
st.title("Weather App")
city = st.text_input("Enter city name", "New York")

if st.button("Get Weather"):
    data = get_weather(city)
    if data["cod"] != "404":
        if "main" in data and "wind" in data and "weather" in data:
            main = data["main"]
            wind = data["wind"]
            weather_desc = data["weather"][0]["description"]

            st.subheader(f"Weather in {city}")
            st.write(f"Temperature: {main['temp']}°K")
            st.write(f"Humidity: {main['humidity']}%")
            st.write(f"Pressure: {main['pressure']} hPa")
            st.write(f"Wind Speed: {wind['speed']} m/s")
            st.write(f"Description: {weather_desc}")
        else:
            st.error("Error: Unexpected response format from OpenWeatherMap API.")
    else:
        st.error("City Not Found!")
