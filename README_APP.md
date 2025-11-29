# AdEase Time Series Forecasting Application

## Overview
This Streamlit application provides comprehensive time series analysis and forecasting for AdEase's Wikipedia page view data to optimize ad placement strategies.

## Features

### 1. **Data Overview**
- View raw and preprocessed data samples
- Aggregated data by language
- Basic statistics (total pages, date range)

### 2. **Exploratory Data Analysis (EDA)**
- Language distribution visualization
- Access type distribution (All-access, Mobile-web, Desktop)
- Access origin distribution (Agents, Spider)
- Interactive time series plots by language

### 3. **Case Study Insights** ⭐ NEW
Comprehensive analysis with detailed descriptions from the case study:
- **Problem Statement**: Understanding page views for 550 days across 145k Wikipedia pages
- **Language Distribution**: English has the highest number of pages
- **Access Patterns**: Distribution of access types and origins
- **Time Series Analysis**: English language trends with seasonality and peaks
- **Decomposition**: Trend, Seasonality, and Residuals visualization
- **Stationarity Testing**: Dickey-Fuller test results and differencing analysis
- **Model Comparison**: ARIMA, SARIMAX, and Prophet performance metrics
- **Business Recommendations**: Strategic insights for ad placement by language

### 4. **Stationarity Test**
- Dickey-Fuller test for all languages
- Interactive differencing analysis
- Visual representation of differenced series

### 5. **Forecasting Models**
Interactive forecasting with multiple models:
- **Exponential Smoothing**: Trend and seasonal components
- **ARIMA**: AutoRegressive Integrated Moving Average
- **SARIMAX**: Seasonal ARIMA with exogenous variables (for English)
- **Prophet**: Facebook's forecasting tool with exogenous support

Performance metrics displayed:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)

### 6. **Logging**
- Comprehensive logging to `app.log`
- View logs directly in the UI via expandable section

## Running the Application

### Prerequisites
```bash
pip install streamlit pandas numpy matplotlib seaborn statsmodels scikit-learn prophet
```

### Launch
```bash
streamlit run app.py
```

The app will be available at: **http://localhost:8501**

## Data Files Required
- `Ad_ease_data/train_1.csv`: Wikipedia page view data (145k pages × 550 days)
- `Ad_ease_data/Exog_Campaign_eng`: Exogenous campaign data for English pages

## Key Insights from Case Study

### Language Performance
1. **English** - Clear winner (High visits, Low MAPE ~0.053)
2. **Russian** - Good conversion potential (Decent visits, Low MAPE ~0.048)
3. **Spanish** - High visits but highest MAPE (~0.086)
4. **Chinese** - Lowest visits (avoid unless specific strategy)
5. **French, German, Japanese** - Medium performance

### Model Performance (English Language)
- **SARIMAX with Exog**: ~0.053 MAPE (Best)
- **Prophet**: ~0.059 MAPE
- **ARIMA**: ~0.074 MAPE

### Recommendations
- Maximize ad placement on **English** pages
- Use **SARIMAX** model for English forecasting (includes campaign effects)
- Consider **Russian** pages for targeted conversion campaigns
- Exercise caution with **Spanish** pages despite high traffic

## Technical Details

### Time Series Characteristics
- **Seasonality**: Weekly patterns (period=7)
- **Trend**: Upward trend in English page views
- **Stationarity**: Most series require 1st order differencing
- **Exogenous Variables**: Campaign dates significantly impact English page views

### Model Parameters (English - Best Performance)
- SARIMAX: (p=2, d=1, q=2) × (P=1, D=1, Q=2, s=7)
- Includes exogenous campaign variable
- MAPE: 0.04052

## Files Created
- `app.py`: Main Streamlit application
- `adease_time_series.py`: Standalone Python script
- `app.log`: Application logs
- `README_APP.md`: This documentation

## Navigation
Use the sidebar to navigate between different sections of the analysis.

---
**Note**: The "Case Study Insights" tab provides the most comprehensive overview with all graphs and detailed descriptions from the original case study.
