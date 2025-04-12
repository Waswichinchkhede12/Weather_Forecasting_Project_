import streamlit as st
import numpy as np
import pandas as pd
import joblib
import datetime

model = joblib.load('weather_model.pkl')
scaler = joblib.load('scaler.pkl')

# Title with Center Alignment
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌤️ Weather Prediction App 🌤️</h1>", unsafe_allow_html=True)

st.markdown("---")

# Creating 2 Columns Layout
col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input("🌡️ Temperature (°C)", step=0.1)
    humidity = st.number_input("💧 Humidity (%)", step=0.1)
    wind_speed = st.number_input("💨 Wind Speed", step=0.1)
    precipitation = st.number_input("🌧️ Precipitation", step=0.1)

with col2:
    wind_direction = st.number_input("🧭 Wind Direction (°)", step=1.0)
    pressure = st.number_input("📈 Pressure", step=0.1)
    cloud_coverage = st.number_input("☁️ Cloud Coverage (%)", step=0.1)

st.markdown("---")

st.markdown("### 📅 Select Date and Time for Prediction")

date = st.date_input("Date")
time = st.time_input("Time")

st.markdown("---")

# Predict Button
if st.button("🔍 Predict Weather"):
    
    date_time = datetime.datetime.combine(date, time)

    hour = date_time.hour
    month = date_time.month
    day = date_time.day

    wind_x = wind_speed * np.cos(np.deg2rad(wind_direction))
    wind_y = wind_speed * np.sin(np.deg2rad(wind_direction))
    is_rain = 1 if precipitation > 0 else 0

    input_data = np.array([[temperature, humidity, wind_speed, wind_direction, pressure,
                            precipitation, cloud_coverage, wind_x, wind_y,
                            hour, month, day, is_rain]])

    input_scaled = scaler.transform(input_data)

    pred = model.predict(input_scaled)[0]

    weather_map = {0: '☀️ Clear', 1: '☁️ Cloudy', 2: '🌧️ Rainy',3:'🌬️ Windy'}

    prediction = weather_map[pred]

    st.success(f"## Predicted Weather is : {prediction}")

    st.markdown("---")

    st.markdown("### 📝 Weather Summary")
    st.info(f"""
    - Temperature: {temperature} °C
    - Humidity: {humidity} %
    - Wind Speed: {wind_speed}
    - Pressure: {pressure}
    - Precipitation: {precipitation}
    - Cloud Coverage: {cloud_coverage} %
    """)

    if 'Clear' in prediction:
        st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGl4ZnptNDNkMnU4eTI2bTBzNGw5bHk5aWFtMjVnZmVwN2tzbjJyMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/0Styincf6K2tvfjb5Q/giphy.gif", caption="It's a Bright & Sunny Day 😎")
        
    elif 'Cloudy' in prediction:
        st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbHVzcHo0OW1jZHVyeHZmaGMzN21zcDNoYnM2OXZ5Y2hiaGdpcDB5MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ef74CyYmtqf31rd1IQ/giphy.gif", caption="Looks Cloudy Outside ☁️")
        
    elif 'Rainy' in prediction:
        st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdW1sMjl0aG1nbmRiM3UyenIwMjA2OGYyc2Fwc2hsdHJubWdzeHV5OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UsMAPgAP1wjW7Coxw2/giphy.gif", caption="Rain is Coming... Take Umbrella ☔")
    else:
        st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzFmbzhtcTY0eDd1Y2k3eHVodGp0MXdkemoxb21nNjlxOW56N2JybyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/G5n8sqIOxBqow/giphy.gif", caption="Strong Winds Blowing — Stay Safe 🌬️")

