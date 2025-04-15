# Weather Forecast Prediction

---

## 🌤️ Project Overview

This project aims to predict weather conditions (Clear, Cloudy, or Rainy) using **machine learning models** based on environmental parameters such as temperature, humidity, pressure, wind speed/direction, and precipitation.  
The pipeline includes **data cleaning**, **model training**, **web deployment with Streamlit**, and **interactive visualization with Power BI**.

The final solution enables users to input weather values and receive real-time predictions, while also exploring insightful patterns and trends using an interactive dashboard.

---

## Features ✨

### 🧹 Data Cleaning & Preprocessing
- Removed missing values, handled duplicates, and outliers for robust model training.
- Converted raw wind data into wind vector components (`wind_x`, `wind_y`) for better prediction accuracy.
- Engineered new features such as:
  - `hour`, `day`, `month` from datetime
  - `is_rain` binary flag from precipitation
- Final dataset exported and used for both model training and visualization.

---

### 🤖 Machine Learning Model
- **Model Used:** Random Forest Classifier
- **Target Classes:** Clear (☀️), Cloudy (☁️), Rainy (🌧️)
- **Input Features:** Temperature, Humidity, Pressure, Wind Speed/Direction, Precipitation, Cloud Coverage, Time & Date
- **Performance Metrics:** Accuracy, Confusion Matrix, and Real-time classification via Streamlit
- **Model Export:** Trained model (`weather_model.pkl`) and scaler (`scaler.pkl`) saved using Joblib

---

### 🌐 Streamlit App
- **User Interface Features:**
  - Clean dark-themed layout with animated weather icons
  - Input widgets for temperature, humidity, wind, etc.
  - Date and time selectors for context-aware prediction
  - Real-time predictions with dynamic summaries and GIF-based feedback
- **Output:** Displays predicted weather condition with visual cues and weather summary

---

### 📊 Power BI Dashboard
- **KPIs Tracked:**
  - Weather condition frequency (Clear, Cloudy, Rainy)
  - Time-based distribution (hourly, daily, monthly)
  - Precipitation and pressure trends
- **Visualizations:**
  - Weather pattern trends
  - Condition distribution over time
  - Interactive filters for date and conditions
- **Interactive Elements:** Slicers for time, condition, and metrics comparison

---

## Tools & Technologies Used 🛠️

| Purpose               | Tools / Libraries                              |
|-----------------------|------------------------------------------------|
| Data Processing       | Python (Jupyter Notebook), Pandas, NumPy       |
| Modeling              | Scikit-learn (Random Forest Classifier)        |
| Deployment            | Streamlit, Joblib                              |
| Visualization         | Power BI                                       |
| Interface Design      | Streamlit widgets, HTML/CSS in markdown        |

---

## 🔍 Key Insights
- Wind vector direction and humidity played a crucial role in rain prediction.
- Cloud coverage and pressure showed strong correlation with cloudy weather.
- Power BI dashboard helped identify daily and seasonal weather variations.

---

## How to Use 🚀

### 1. **Machine Learning Model**
- Open `MachineLearningModel.ipynb` in Jupyter Notebook to view the full data preprocessing and model training process.
- Evaluate predictions, check accuracy, and export the final model and scaler using Joblib.

### 2. **Streamlit Web App**
- Run `WeatherPredictionApp.py` to launch the live prediction interface.
```bash
streamlit run app.py
```
- Enter values and get instant weather predictions!

### 3. **Power BI Dashboard**
- Open `weather_forecast.pbix` in Power BI Desktop.
- Explore different KPIs and analyze patterns in weather behavior.

---

## 📁 Project Files

| File Name                        | Description                                                |
|----------------------------------|------------------------------------------------------------|
| `MachineLearningModel.ipynb`    | Jupyter notebook with preprocessing and ML training        |
| `WeatherPredictionApp.py`       | Streamlit app for live weather prediction                  |
| `weather_model.pkl`             | Trained Random Forest model                                |
| `scaler.pkl`                    | Scaler used for model input normalization                  |
| `Streamlit.png`                 | Screenshot of deployed web interface                       |
| `weather_forecast.pbix`         | Power BI dashboard for insights and data storytelling      |

---


## Acknowledgments 🙌

- **[Akash Singh Rathore]**: Data Cleaning 
- **[Aditya]**: Model Development, Streamlit Integration  
- **[Your Teammates (if any)]**: Power BI Dashboard, Data Engineering  
- Special thanks to the hackathon mentors & organizers for support and guidance!

---

## 📌 Final Note

This project showcases the power of combining **machine learning**, **real-time prediction**, and **visual storytelling** to help people understand and anticipate weather patterns.  
Whether for planning events, optimizing logistics, or just grabbing an umbrella — this app brings data to life. ☁️🌞🌧️

---
