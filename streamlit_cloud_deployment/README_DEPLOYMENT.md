# 🚀 Streamlit Cloud Deployment Version

This folder contains an **optimized version** of the AdEase Time Series app specifically for Streamlit Cloud deployment.

## 🔧 Optimizations Applied

### Memory Efficiency
- **Downcast Data Types**: Float64 → Float32, Int64 → Int32 (saves ~50% memory)
- **Smart Data Loading**: Automatically finds data files in parent directory (uses Git LFS)
- **Reduced Copies**: Minimized unnecessary data duplication

### Why a Separate Folder?
The main `app.py` in the root directory is optimized for **local development** with full memory resources. This deployment version is specifically tuned for **Streamlit Cloud's free tier** memory limits.

## 📦 Deployment Instructions

### Option 1: Deploy from this Subdirectory
1. Go to [share.streamlit.io](https://share.streamlit.io/)
2. Click **"New App"**
3. Repository: `Ratnesh-181998/AdEase-Time-Series-Analysis`
4. Branch: `main`
5. **Main file path**: `streamlit_cloud_deployment/app.py` ⚠️ (Important!)
6. Click **"Deploy"**

### Option 2: Deploy from Root (Alternative)
If you prefer to deploy from the root directory:
1. Replace the root `app.py` with `streamlit_cloud_deployment/app.py`
2. Deploy with main file path: `app.py`

## 📊 Data Handling
- The large `train_1.csv` (265MB) is stored via **Git LFS** in the root `Ad_ease_data/` folder
- This deployment version automatically looks for data in `../Ad_ease_data/` (parent directory)
- Streamlit Cloud will automatically download LFS files during deployment

## ✅ What's Different?
| Feature | Root `app.py` | Deployment `app.py` |
|---------|---------------|---------------------|
| Memory Usage | Standard (float64/int64) | Optimized (float32/int32) |
| Data Path | `Ad_ease_data/` | `../Ad_ease_data/` or `Ad_ease_data/` |
| Target | Local Development | Streamlit Cloud |

## 🎯 Expected Behavior
- ✅ Loads in ~10-15 seconds on Streamlit Cloud
- ✅ Uses ~50% less memory than standard version
- ✅ All features work identically to local version
- ✅ No loss of accuracy (float32 is sufficient for this data)

## 🐛 Troubleshooting
If deployment fails:
1. Check that Git LFS is enabled on your repo
2. Verify `train_1.csv` is tracked by LFS (`.gitattributes`)
3. Ensure the main file path is set to `streamlit_cloud_deployment/app.py`

---

**Author**: Ratnesh Singh  
**Contact**: rattudacsit2021gate@gmail.com
