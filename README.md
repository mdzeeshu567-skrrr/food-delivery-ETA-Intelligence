# Food Delivery ETA & Delay Intelligence

An end-to-end data analytics and machine learning project that predicts food delivery times and identifies orders at risk of delay.

## Project Overview

This project combines data analysis, machine learning, SQL Server, Power BI, and Streamlit to explore delivery performance and provide delivery-time predictions.

## Objectives

- Predict estimated delivery time (ETA).
- Classify orders as delayed or not delayed.
- Analyze delivery performance using SQL.
- Identify patterns related to traffic, weather, distance, vehicle type, and festivals.
- Present insights through a Power BI dashboard.
- Provide an interactive prediction interface using Streamlit.

## Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- SQL Server
- Power BI
- Streamlit
- Git and GitHub

## Machine Learning Models

### ETA Prediction
A tuned Random Forest regression model achieved the following test results:

| Metric | Result |
|---|---:|
| Mean Absolute Error (MAE) | 4.64 minutes |
| Root Mean Squared Error (RMSE) | 5.90 minutes |
| R² Score | 0.604 |

### Delay Classification
A Random Forest classifier identifies orders likely to take longer than 34 minutes.

| Metric | Result |
|---|---:|
| Accuracy | 87% |
| ROC-AUC | 0.928 |
| Delayed-class F1-score | 0.68 |

These results are from the project's current evaluation and may vary with further validation.

## SQL Analysis

SQL Server was used to analyze 45,593 delivery records.

Key findings include:
- Average delivery time: 26.29 minutes.
- Overall delay rate: 19.38%, using a threshold of more than 34 minutes.
- Higher average delivery times were observed in the Jam traffic category.
- Delivery times varied across weather conditions and distances.

These are observed associations, not proof that any single factor causes delays.

## Project Files

| File | Description |
|---|---|
| `app.py` | Streamlit prediction application |
| `01_Data_Understanding.py` | Data understanding and analysis |
| `delivery_analysis.sql` | SQL analysis queries |
| `Food_Delivery_ETA_Intelligence.pbix` | Power BI dashboard |
| `food_delivery_cleaned_checkpoint.csv` | Cleaned dataset checkpoint |

## How to Run the Application

1. Install Python.
2. Clone or download this repository.
3. Install the required Python packages.
4. Ensure the trained model files are available in the project directory.
5. Run the application:

```bash
streamlit run app.py
```

Note: A `requirements.txt` file and trained model files must be included or created separately for a complete reproducible setup.

## Disclaimer

Predictions are estimates based on historical data and are not guaranteed delivery times.

## Author

**Md Zeeshan**
