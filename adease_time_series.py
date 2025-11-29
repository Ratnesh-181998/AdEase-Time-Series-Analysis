import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from locale import normalize
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error as mse, mean_absolute_error as mae, mean_absolute_percentage_error as mape

# Suppress warnings
warnings.filterwarnings('ignore')

# Display options
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 1000)
pd.options.display.max_colwidth = 1000
sns.set(style='darkgrid')

# Load data
# Adjusted paths for local execution
try:
    df = pd.read_csv("Ad_ease_data/train_1.csv")
    Exog_Campaign_eng = pd.read_csv("Ad_ease_data/Exog_Campaign_eng")
except FileNotFoundError:
    print("Data files not found in Ad_ease_data directory. Please ensure train_1.csv and Exog_Campaign_eng are present.")
    # Fallback to check current directory just in case
    try:
        df = pd.read_csv("train_1.csv")
        Exog_Campaign_eng = pd.read_csv("Exog_Campaign_eng")
    except:
        pass

# Data Exploration
print("Data Shape:", df.shape)
print("Exog Shape:", Exog_Campaign_eng.shape)

data = df.copy()
print("Duplicates:", data.duplicated().sum())

# Fill NaN with 0
data.fillna(0, inplace=True)

# Extract Language
def Extract_Language(name):
    if len(re.findall(r'_(.{2}).wikipedia.org_', name)) == 1:
        return re.findall(r'_(.{2}).wikipedia.org_', name)[0]
    else:
        return 'Unknown'

data["Language"] = data["Page"].map(Extract_Language)

dict_ = {
    'de': 'German',
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'ja': 'Japenese',
    'ru': 'Russian',
    'zh': 'Chinese',
    'Unknown': 'Unknown_Language'
}
data["Language"] = data["Language"].map(dict_)

# Plot Language Distribution
plt.figure(figsize=(10, 5))
data.groupby("Language")["Page"].count().plot(kind="bar")
plt.xlabel("Language")
plt.ylabel("Number of Pages")
plt.title("Number of Pages per each language")
plt.show()

# Extract Access Type
data["Access_Type"] = data.Page.str.findall(r'all-access|mobile-web|desktop').apply(lambda x: x[0])

plt.figure(figsize=(8, 8))
x = (data["Access_Type"].value_counts(dropna=False, normalize=True) * 100).values
y = (data["Access_Type"].value_counts(dropna=False, normalize=True) * 100).index
plt.pie(x, labels=y, radius=1.5, autopct='%1.1f%%', pctdistance=0.5)
plt.title('Access_Type Distribution', fontsize=10, fontweight='bold')
plt.axis('equal')
plt.show()

# Extract Access Origin
data["Access_Origin"] = data.Page.str.findall(r'spider|agents').apply(lambda x: x[0])

plt.figure(figsize=(8, 8))
x = (data["Access_Origin"].value_counts(dropna=False, normalize=True) * 100).values
y = (data["Access_Origin"].value_counts(dropna=False, normalize=True) * 100).index
plt.pie(x, labels=y, radius=1.5, autopct='%1.1f%%', pctdistance=0.5)
plt.title('Access_Origin Distribution', fontsize=15, fontweight='bold')
plt.axis('equal')
plt.show()

# Aggregating data by Language
aggregated_data = data.groupby("Language").mean().T.drop("Unknown_Language", axis=1).reset_index()
aggregated_data["index"] = pd.to_datetime(aggregated_data["index"])
aggregated_data = aggregated_data.set_index("index")

# Plot Time Series for each language
plt.rcParams['figure.figsize'] = (20, 15)
aggregated_data.plot()
plt.xlabel("Time Index")
plt.ylabel("Visits Per Each Language")
plt.show()

# Stationarity Test
def Dickey_Fuller_test(ts, significances_level=0.05):
    p_value = sm.tsa.stattools.adfuller(ts)[1]
    if p_value <= significances_level:
        print("Time Series is Stationary")
    else:
        print("Time Series is NOT Stationary")
    print("P_value is: ", p_value)

for Language in aggregated_data.columns:
    print(Language)
    Dickey_Fuller_test(aggregated_data[Language], significances_level=0.05)
    print()

# Analysis for English Language
TS_English = aggregated_data.English

def adf_test(timeseries):
    print('Results of Dickey-Fuller Test:')
    dftest = sm.tsa.stattools.adfuller(timeseries, autolag='AIC')
    df_output = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        df_output['Critical Value (%s)' % key] = value
    print(df_output)

adf_test(TS_English)

# Decomposition
plt.rcParams['figure.figsize'] = (15, 10)
Decomposition_model = seasonal_decompose(TS_English, model='additive', period=7)
Decomposition_model.plot()
plt.show()

print("Stationarity of Residuals:")
Dickey_Fuller_test(pd.Series(Decomposition_model.resid).fillna(0))

# Differencing
print("Stationarity after differencing:")
Dickey_Fuller_test(TS_English.diff(1).dropna())

# Performance Metrics
def performance(actual, predicted):
    print('MAE :', round(mae(actual, predicted), 3))
    print('RMSE :', round(mse(actual, predicted)**0.5, 3))
    print('MAPE:', round(mape(actual, predicted), 3))

# Exponential Smoothing
X_train = TS_English.loc[TS_English.index < TS_English.index[-30]].copy()
X_test = TS_English.loc[TS_English.index >= TS_English.index[-30]].copy()

model_es = ExponentialSmoothing(X_train, trend="add", damped_trend="add", seasonal="add")
model_es = model_es.fit()
Pred_es = model_es.forecast(steps=30)

print("Exponential Smoothing Performance:")
performance(X_test, Pred_es)

plt.figure(figsize=(20, 8))
X_test.plot(style="-o", label="Test_data")
Pred_es.plot(label="Predicted_data")
plt.legend()
plt.title("Exponential Smoothing Forecast")
plt.show()

# ARIMA
n_forecast = 30
model_arima = ARIMA(TS_English[:-n_forecast], order=(1, 1, 1))
model_arima = model_arima.fit()
predicted_arima = model_arima.forecast(steps=n_forecast, alpha=0.05)

print("ARIMA Performance:")
performance(TS_English.values[-n_forecast:], predicted_arima.values)

plt.figure(figsize=(20, 8))
TS_English.plot(label='Actual')
predicted_arima.plot(label='Forecast', linestyle='dashed', marker='o', markerfacecolor='green', markersize=2)
plt.legend(loc="upper right")
plt.title('ARIMA BASE Model (1,1,1) : Actual vs Forecasts', fontsize=15, fontweight='bold')
plt.show()

# SARIMAX
def sarimax_model(time_series, n, p=0, d=0, q=0, P=0, D=0, Q=0, s=0, exog=[]):
    # Creating SARIMAX Model
    if len(exog) > 0:
        model = SARIMAX(time_series[:-n],
                        order=(p, d, q),
                        seasonal_order=(P, D, Q, s),
                        exog=exog[:-n],
                        initialization='approximate_diffuse')
        model_fit = model.fit()
        model_forecast = model_fit.forecast(n, dynamic=True, exog=pd.DataFrame(exog[-n:]))
    else:
        model = SARIMAX(time_series[:-n],
                        order=(p, d, q),
                        seasonal_order=(P, D, Q, s),
                        initialization='approximate_diffuse')
        model_fit = model.fit()
        model_forecast = model_fit.forecast(n, dynamic=True)
    
    # Plotting
    plt.figure(figsize=(20, 8))
    time_series[-60:].plot(label='Actual')
    model_forecast[-60:].plot(label='Forecast', color='red', linestyle='dashed', marker='o', markerfacecolor='green', markersize=5)
    plt.legend(loc="upper right")
    plt.title(f'SARIMAX Model ({p},{d},{q}) ({P},{D},{Q},{s}) : Actual vs Forecasts', fontsize=15, fontweight='bold')
    plt.show()
    
    # Metrics
    actuals = time_series.values[-n:]
    errors = time_series.values[-n:] - model_forecast.values
    mape_val = np.mean(np.abs(errors) / np.abs(actuals))
    rmse_val = np.sqrt(np.mean(errors**2))
    print()
    print(f'MAPE of Model : {np.round(mape_val, 5)}')
    print(f'RMSE of Model : {np.round(rmse_val, 3)}')

# SARIMAX Grid Search (Simplified)
def SARIMAX_grid_search(time_series, n, param, d_param, s_param, exog=[]):
    counter = 0
    param_df = pd.DataFrame(columns=['serial', 'pdq', 'PDQs', 'mape', 'rmse'])
    
    # Nested loops for grid search (simplified for brevity/correctness based on PDF)
    # The PDF had a very deep nesting which might be slow to run.
    # I will include the structure but maybe not run it fully if it takes too long.
    # But the user asked for the code, so I should provide it.
    
    for p in param:
        for d in d_param:
            for q in param:
                for P in param:
                    for D in d_param:
                        for Q in param:
                            for s in s_param:
                                try:
                                    if len(exog) > 0:
                                        model = SARIMAX(time_series[:-n],
                                                        order=(p, d, q),
                                                        seasonal_order=(P, D, Q, s),
                                                        exog=exog[:-n],
                                                        initialization='approximate_diffuse')
                                        model_fit = model.fit(disp=False)
                                        model_forecast = model_fit.forecast(n, dynamic=True, exog=pd.DataFrame(exog[-n:]))
                                    else:
                                        model = SARIMAX(time_series[:-n],
                                                        order=(p, d, q),
                                                        seasonal_order=(P, D, Q, s),
                                                        initialization='approximate_diffuse')
                                        model_fit = model.fit(disp=False)
                                        model_forecast = model_fit.forecast(n, dynamic=True)

                                    actuals = time_series.values[-n:]
                                    errors = time_series.values[-n:] - model_forecast.values
                                    mape_val = np.mean(np.abs(errors) / np.abs(actuals))
                                    rmse_val = np.sqrt(np.mean(errors**2))
                                    
                                    counter += 1
                                    list_row = [counter, (p, d, q), (P, D, Q, s), np.round(mape_val, 5), np.round(rmse_val, 3)]
                                    param_df.loc[len(param_df)] = list_row
                                    print(f'Combination {counter}: MAPE={mape_val:.5f}')
                                except Exception as e:
                                    continue
    return param_df

# Example usage for English (commented out to avoid long run time, or user can uncomment)
# exog = Exog_Campaign_eng['Exog'].to_numpy()
# time_series = aggregated_data.English
# n = 30
# param = [0, 1, 2]
# d_param = [0, 1]
# s_param = [7]
# english_params = SARIMAX_grid_search(time_series, n, param, d_param, s_param, exog)

# Best parameters for English from PDF
# Parameters of Model : (2,0,1) (0,1,2,7)
print("Running Best SARIMAX for English...")
exog = Exog_Campaign_eng['Exog'].to_numpy()
time_series = aggregated_data.English
n = 30
sarimax_model(time_series, n, p=2, d=0, q=1, P=0, D=1, Q=2, s=7, exog=exog)

# Prophet
try:
    from prophet import Prophet
    print("Running Prophet...")
    
    time_series_prophet = aggregated_data.reset_index()[['index', 'English']]
    time_series_prophet.columns = ['ds', 'y']
    time_series_prophet['exog'] = Exog_Campaign_eng['Exog'].values
    
    prophet = Prophet(weekly_seasonality=True)
    prophet.add_regressor('exog')
    prophet.fit(time_series_prophet[:-30])
    
    future = prophet.make_future_dataframe(periods=30, freq='D')
    future['exog'] = Exog_Campaign_eng['Exog'].values # Need exog for future too? 
    # The PDF code used `prophet2.predict(time_series)` which implies predicting on history + future?
    # The PDF code:
    # prophet2.fit(time_series[:-30])
    # forecast2 = prophet2.predict(time_series)
    
    forecast = prophet.predict(time_series_prophet)
    
    prophet.plot(forecast)
    plt.show()
    
    actual = time_series_prophet['y'].values
    pred = forecast['yhat'].values
    
    plt.figure(figsize=(20, 8))
    plt.plot(actual, label='Actual')
    plt.plot(pred, label='Forecast', color='red', linestyle='dashed')
    plt.legend()
    plt.title('Prophet Model (With Exogenous variable)')
    plt.show()
    
    performance(actual, pred)

except ImportError:
    print("Prophet not installed. Skipping Prophet section.")
except Exception as e:
    print(f"Prophet error: {e}")

