# 📊 AdEase AI Forecasting Engine

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**AdEase AI Forecasting Engine** is a powerful time series analysis and forecasting system designed to optimize digital ad placements. It leverages advanced statistical models (ARIMA, SARIMAX) and machine learning (Facebook Prophet) to predict future page views across multiple languages, enabling data-driven marketing strategies.

---

## 🚀 Key Features

### 1. 📊 Data Overview
- **Real-time Metrics:** Instant view of total pages, languages, data points, and total views.
- **Data Inspection:** Interactive tables for raw data, processed features, and aggregated language metrics.
- **Visual Hierarchy:** Clean, organized layout with colorful metric indicators.

### 2. 🔍 Exploratory Data Analysis (EDA)
- **Interactive Visualizations:** Dynamic charts for language distribution, access types (Mobile vs. Desktop), and traffic origins (Agent vs. Spider).
- **Time Series Plots:** Compare traffic trends across different languages with adjustable date ranges.
- **Quick Insights:** Automated summary boxes highlighting key data patterns.

### 3. 📈 Case Study Insights
- **Business Context:** Detailed problem statement and objectives.
- **Deep Dive:** In-depth analysis of specific segments (e.g., English language dominance).
- **Visual Storytelling:** Curated plots and inferences directly from the case study.

### 4. 📉 Stationarity & Statistical Tests
- **Dickey-Fuller Test:** Automated stationarity testing for all languages with clear ✅/❌ indicators.
- **Differencing Tool:** Interactive tool to apply and visualize differencing (d=1, d=2) to make series stationary.
- **Educational Content:** Built-in explanations of why stationarity matters for forecasting.

### 5. 🔮 Advanced Forecasting
- **Multi-Model Support:**
  - **Exponential Smoothing:** For baseline trend/seasonality.
  - **ARIMA:** Classic autoregressive integrated moving average.
  - **SARIMAX:** Seasonal ARIMA with Exogenous variables (Campaign data).
  - **Facebook Prophet:** Robust forecasting with holiday/event support.
- **Interactive Controls:** Adjust forecast horizon (7-60 days) and select specific languages.
- **Performance Metrics:** Real-time calculation of MAPE, RMSE, and MAE.

### 6. 📚 Complete Analysis Walkthrough
- **Full Case Study:** A dedicated tab mirroring the original case study structure.
- **Step-by-Step Guide:** From data cleaning to final recommendations.
- **Code & Math:** View the underlying Python code and mathematical formulas.

### 7. 🎨 Modern UI/UX
- **Dark Mode Aesthetic:** Sleek dark theme with high-contrast text.
- **Glassmorphism:** Modern translucent elements and gradients.
- **Responsive Design:** Optimized for various screen sizes.

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Data Manipulation:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Forecasting:** Statsmodels (ARIMA/SARIMAX), Facebook Prophet
- **Machine Learning:** Scikit-learn (Metrics)

---

## ⚙️ Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Ratnesh-181998/AdEase-AI-Forecasting-Engine.git
    cd AdEase-AI-Forecasting-Engine
    ```

2.  **Create a Virtual Environment (Optional but Recommended)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application**
    ```bash
    streamlit run app.py
    ```

---

## 📂 Project Structure

```
AdEase-AI-Forecasting-Engine/
├── Ad_ease_data/          # Dataset files
├── app.py                 # Main Streamlit application
├── adease_time_series.py  # Core analysis logic
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── LICENSE                # MIT License
└── .gitignore             # Git ignore rules
```

---

## 📞 Contact

**RATNESH SINGH**

- 📧 **Email:** [rattudacsit2021gate@gmail.com](mailto:rattudacsit2021gate@gmail.com)
- 💼 **LinkedIn:** [https://www.linkedin.com/in/ratneshkumar1998/](https://www.linkedin.com/in/ratneshkumar1998/)
- 🐙 **GitHub:** [https://github.com/Ratnesh-181998](https://github.com/Ratnesh-181998)
- 📱 **Phone:** +91-947XXXXX46

### Project Links
- 🐛 **Issue Tracker:** [GitHub Issues](https://github.com/Ratnesh-181998/AdEase-AI-Forecasting-Engine/issues)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
