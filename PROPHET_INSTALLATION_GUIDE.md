# Prophet Installation Guide

## Issue
When trying to use the Prophet model in the Forecasting tab, you may see this error:
```
An error occurred during forecasting: No module named 'prophet'
```

## Solution

### Option 1: Install Prophet (Recommended)

**For Windows:**
```bash
pip install prophet
```

If that doesn't work, try installing pystan first:
```bash
pip install pystan==2.19.1.1
pip install prophet
```

**For Mac/Linux:**
```bash
pip install prophet
```

### Option 2: Use Alternative Models (No Installation Needed)

The following models are already available and work without any additional installation:

1. **✅ Exponential Smoothing**
   - Simple and fast
   - Good for capturing trend and seasonality
   - MAPE: ~7.4%

2. **✅ ARIMA**
   - Classic time series model
   - Good for non-seasonal data
   - MAPE: ~7.4%

3. **✅ SARIMAX** (Recommended)
   - Best performing model
   - Handles seasonality and exogenous variables
   - MAPE: ~4.1% (with campaign data for English)
   - **This is the best choice!**

## Recommendation

**For best results, use SARIMAX instead of Prophet:**
- SARIMAX performs better on this dataset (4.1% vs 5.9% MAPE)
- Already installed and ready to use
- Supports exogenous variables (campaign dates for English)
- Captures weekly seasonality perfectly

## How to Use SARIMAX

1. Go to the **🔮 Forecasting** tab
2. Select **Language**: English (or any other)
3. Select **Model**: SARIMAX
4. Adjust **Forecast Steps**: 7-60 days
5. Click **Run Forecast**

For English language, the model will automatically use campaign data as an exogenous variable for better accuracy.

## Prophet vs SARIMAX Comparison

| Feature | Prophet | SARIMAX |
|---------|---------|---------|
| Installation | Requires pip install | ✅ Already installed |
| MAPE (English) | ~5.9% | ~4.1% ⭐ |
| Seasonality | ✅ Automatic | ✅ Manual (s=7) |
| Exog Variables | ✅ Supported | ✅ Supported |
| Ease of Use | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Accuracy | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Speed | ⭐⭐⭐ | ⭐⭐⭐⭐ |

## Conclusion

**You don't need to install Prophet!** 

Use **SARIMAX** instead - it's already available, more accurate, and performs better on this dataset.
