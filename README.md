# 📊 AdEase AI Forecasting Engine

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**AdEase AI Forecasting Engine** is a powerful time series analysis and forecasting system designed to optimize digital ad placements. It leverages advanced statistical models (ARIMA, SARIMAX) and machine learning (Facebook Prophet) to predict future page views across multiple languages, enabling data-driven marketing strategies.

---

## 🎬 Demo
- **Streamlit Profile** - https://share.streamlit.io/user/ratnesh-181998
- **Project Demo** - https://adease-time-series-analysis-drkta7i8zeotm6ayyasjj8.streamlit.app/
  
---
## 🚀 Key Features

### 1. 📊 Data Overview
- **Real-time Metrics:** Instant view of total pages, languages, data points, and total views.
- **Data Inspection:** Interactive tables for raw data, processed features, and aggregated language metrics.
- **Visual Hierarchy:** Clean, organized layout with colorful metric indicators.
- 
<img width="2879" height="1687" alt="image" src="https://github.com/user-attachments/assets/eea54399-b2ed-4b41-bdc5-ba3e5bfbe093" />
<img width="2851" height="1636" alt="image" src="https://github.com/user-attachments/assets/21fa3421-e3fc-41f2-8acd-527ccdbfa635" />


### 2. 🔍 Exploratory Data Analysis (EDA)
- **Interactive Visualizations:** Dynamic charts for language distribution, access types (Mobile vs. Desktop), and traffic origins (Agent vs. Spider).
- **Time Series Plots:** Compare traffic trends across different languages with adjustable date ranges.
- **Quick Insights:** Automated summary boxes highlighting key data patterns.

<img width="2860" height="1718" alt="image" src="https://github.com/user-attachments/assets/ee46278b-3510-474b-82b5-237859439535" />
<img width="2814" height="1715" alt="image" src="https://github.com/user-attachments/assets/fe2961c1-af2b-4553-82da-8a36cbaf7b38" />
<img width="2875" height="1666" alt="image" src="https://github.com/user-attachments/assets/a7528831-f696-4cc7-9bea-0be566d2f961" />


### 3. 📈 Case Study Insights
- **Business Context:** Detailed problem statement and objectives.
- **Deep Dive:** In-depth analysis of specific segments (e.g., English language dominance).
- **Visual Storytelling:** Curated plots and inferences directly from the case study.

<img width="2871" height="1689" alt="image" src="https://github.com/user-attachments/assets/a748da31-de29-45d0-a9c3-58d44cf3113e" />
<img width="2828" height="1716" alt="image" src="https://github.com/user-attachments/assets/9ce585a4-a97c-42a9-8168-8df672181b73" />
<img width="2775" height="1701" alt="image" src="https://github.com/user-attachments/assets/fe892cc3-7de5-42f9-91a6-a6cde3e5ec92" />
<img width="2873" height="1703" alt="image" src="https://github.com/user-attachments/assets/35be44f3-0c2b-4302-9b37-cafa84ffa6cc" />
<img width="2861" height="1669" alt="image" src="https://github.com/user-attachments/assets/019c9df1-d0b1-4d3f-9d44-cf85f468e348" />
<img width="2843" height="1710" alt="image" src="https://github.com/user-attachments/assets/4d852471-6794-4f1d-94f6-ec2d6edbb2de" />
<img width="2384" height="1445" alt="image" src="https://github.com/user-attachments/assets/3c8e72c3-3c9b-4351-922e-08558e877bc2" />
<img width="2473" height="1248" alt="image" src="https://github.com/user-attachments/assets/eb835625-dfd9-4fae-b318-3bf4af0c1e97" />


### 4. 📉 Stationarity & Statistical Tests
- **Dickey-Fuller Test:** Automated stationarity testing for all languages with clear ✅/❌ indicators.
- **Differencing Tool:** Interactive tool to apply and visualize differencing (d=1, d=2) to make series stationary.
- **Educational Content:** Built-in explanations of why stationarity matters for forecasting.

<img width="2879" height="1726" alt="image" src="https://github.com/user-attachments/assets/0712f147-d848-4036-820e-dd048a926557" />
<img width="2868" height="1706" alt="image" src="https://github.com/user-attachments/assets/5f3a8348-7034-4ff3-8772-a6e8017ee4f3" />
<img width="2850" height="1697" alt="image" src="https://github.com/user-attachments/assets/82e6e633-ed32-432f-b868-7048bdc4abec" />


### 5. 🔮 Advanced Forecasting
- **Multi-Model Support:**
  - **Exponential Smoothing:** For baseline trend/seasonality.
  - **ARIMA:** Classic autoregressive integrated moving average.
  - **SARIMAX:** Seasonal ARIMA with Exogenous variables (Campaign data).
  - **Facebook Prophet:** Robust forecasting with holiday/event support.
- **Interactive Controls:** Adjust forecast horizon (7-60 days) and select specific languages.
- **Performance Metrics:** Real-time calculation of MAPE, RMSE, and MAE.

<img width="2879" height="1657" alt="image" src="https://github.com/user-attachments/assets/c5d2a2e0-f6fa-4f96-ba5e-3a8b643772ad" />
<img width="2879" height="1686" alt="image" src="https://github.com/user-attachments/assets/44b23ca7-a3d6-4911-a15d-670c8f84bca1" />
<img width="2858" height="1706" alt="image" src="https://github.com/user-attachments/assets/1da42d70-ddf7-427b-9d11-859a1403a3f1" />
<img width="2869" height="1697" alt="image" src="https://github.com/user-attachments/assets/7f076aac-9ec6-4324-b7cd-5510a5eb1f78" />
<img width="2415" height="1449" alt="image" src="https://github.com/user-attachments/assets/384dd0f6-3df3-42cd-9d03-bef43ceb1a3b" />
<img width="2418" height="1504" alt="image" src="https://github.com/user-attachments/assets/2057c8b1-ab17-4a2d-9193-03f4e7c5d8b5" />
<img width="2393" height="1477" alt="image" src="https://github.com/user-attachments/assets/6bbf5823-edbe-46b8-800c-0cee0c4b8e4f" />
<img width="2420" height="1433" alt="image" src="https://github.com/user-attachments/assets/2874e27b-fb98-4839-945d-b8441817b4e0" />
<img width="2842" height="1695" alt="image" src="https://github.com/user-attachments/assets/60ff82ab-a3cd-4ec2-8615-49d68b3b7f43" />
<img width="2414" height="1428" alt="image" src="https://github.com/user-attachments/assets/e7bca46b-712a-4d91-9268-ab6762325d3b" />


### 6. 📚 Complete Analysis Walkthrough
- **Full Case Study:** A dedicated tab mirroring the original case study structure.
- **Step-by-Step Guide:** From data cleaning to final recommendations.
- **Code & Math:** View the underlying Python code and mathematical formulas.
<img width="2847" height="1675" alt="image" src="https://github.com/user-attachments/assets/ae1cf4a1-9a53-48c8-9364-ca800068fcb7" />
<img width="2403" height="1401" alt="image" src="https://github.com/user-attachments/assets/e01ca17a-9148-4a14-916d-70933f0f67bc" />
<img width="2339" height="1492" alt="image" src="https://github.com/user-attachments/assets/ad8b9699-841f-4a27-a1fb-cac15c20ed0a" />
<img width="2393" height="1443" alt="image" src="https://github.com/user-attachments/assets/ff61628d-059a-4e5a-b011-5584c6f61ca3" />
<img width="2420" height="1472" alt="image" src="https://github.com/user-attachments/assets/dc987176-3509-4f55-ac8f-26f8cceb6d3d" />
<img width="2796" height="1497" alt="image" src="https://github.com/user-attachments/assets/849bc324-8425-498b-85fa-ab6bd73d0ccb" />
<img width="2371" height="1514" alt="image" src="https://github.com/user-attachments/assets/a5c464dc-066e-42e7-9d02-695c2f8160fd" />
<img width="2281" height="1357" alt="image" src="https://github.com/user-attachments/assets/2937812d-83b6-4cb1-bbbc-9dced7ad5a7e" />
<img width="2381" height="1294" alt="image" src="https://github.com/user-attachments/assets/29f3cee9-88c3-48a0-b9be-6d2602aead40" />
<img width="2392" height="1319" alt="image" src="https://github.com/user-attachments/assets/28718d32-6f78-4b73-afe7-ef04eaebaf14" />
<img width="2399" height="1427" alt="image" src="https://github.com/user-attachments/assets/a98e7344-9382-4095-b460-7935f5ae658f" />
<img width="2373" height="1317" alt="image" src="https://github.com/user-attachments/assets/df593626-2a48-46ee-8945-52653aa8d396" />
<img width="2384" height="1438" alt="image" src="https://github.com/user-attachments/assets/4fda7ea4-6a2e-43bd-b07e-689d6051a028" />
<img width="2360" height="1421" alt="image" src="https://github.com/user-attachments/assets/57c9262b-0d88-44aa-af34-c361aea1eb0d" />
<img width="2325" height="1378" alt="image" src="https://github.com/user-attachments/assets/89e0d771-1f6d-4ced-a8e2-5d1ee8f0cd70" />
<img width="2258" height="1492" alt="image" src="https://github.com/user-attachments/assets/af4141f5-d929-43a8-8a74-12c0be0af70c" />
<img width="2444" height="1471" alt="image" src="https://github.com/user-attachments/assets/0ce254a8-ba5d-44b2-9ea0-f61b86aeec33" />
<img width="2446" height="1501" alt="image" src="https://github.com/user-attachments/assets/d3529d59-4a3c-4544-a27e-c84f84b7403b" />
<img width="2435" height="1441" alt="image" src="https://github.com/user-attachments/assets/e104f6d9-0323-4999-832b-22a94150aefd" />
<img width="2296" height="760" alt="image" src="https://github.com/user-attachments/assets/525bd2fb-9441-43c5-92c2-6a16767caa5a" />

### 7. APP LOGS

<img width="2431" height="1502" alt="image" src="https://github.com/user-attachments/assets/afde2bcd-de97-4785-99da-97b975aa82e8" />
<img width="2455" height="1419" alt="image" src="https://github.com/user-attachments/assets/6f0b412c-4c86-43f3-8e5b-a6c618632bee" />

### 8. 🎨 Modern UI/UX
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
- 🌐 Live Demo: [Streamlit](https://adease-time-series-analysis-drkta7i8zeotm6ayyasjj8.streamlit.app/)
- 📖 Documentation: [GitHub Wiki](https://github.com/Ratnesh-181998/AdEase-Time-Series-Analysis/wiki)
- 🐛 Issue Tracker: [GitHub Issues](https://github.com/Ratnesh-181998/AdEase-Time-Series-Analysis/issues)
  
---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=24,20,12,6&height=3" width="100%">


## 📜 **License**

![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge&logo=opensourceinitiative&logoColor=white)

**Licensed under the MIT License** - Feel free to fork and build upon this innovation! 🚀

---

# 📞 **CONTACT & NETWORKING** 📞


### 💼 Professional Networks

[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ratneshkumar1998/)
[![GitHub](https://img.shields.io/badge/🐙_GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ratnesh-181998)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/RatneshS16497)
[![Portfolio](https://img.shields.io/badge/🌐_Portfolio-FF6B6B?style=for-the-badge&logo=google-chrome&logoColor=white)](https://share.streamlit.io/user/ratnesh-181998)
[![Email](https://img.shields.io/badge/✉️_Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:rattudacsit2021gate@gmail.com)
[![Medium](https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@rattudacsit2021gate)
[![Stack Overflow](https://img.shields.io/badge/Stack_Overflow-F58025?style=for-the-badge&logo=stack-overflow&logoColor=white)](https://stackoverflow.com/users/32068937/ratnesh-kumar)

### 🚀 AI/ML & Data Science
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://share.streamlit.io/user/ratnesh-181998)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/RattuDa98)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/rattuda)

### 💻 Competitive Programming
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/Ratnesh_1998/)
[![HackerRank](https://img.shields.io/badge/HackerRank-00EA64?style=for-the-badge&logo=hackerrank&logoColor=black)](https://www.hackerrank.com/profile/rattudacsit20211)
[![CodeChef](https://img.shields.io/badge/CodeChef-5B4638?style=for-the-badge&logo=codechef&logoColor=white)](https://www.codechef.com/users/ratnesh_181998)
[![Codeforces](https://img.shields.io/badge/Codeforces-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white)](https://codeforces.com/profile/Ratnesh_181998)
[![GeeksforGeeks](https://img.shields.io/badge/GeeksforGeeks-2F8D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white)](https://www.geeksforgeeks.org/profile/ratnesh1998)
[![HackerEarth](https://img.shields.io/badge/HackerEarth-323754?style=for-the-badge&logo=hackerearth&logoColor=white)](https://www.hackerearth.com/@ratnesh138/)
[![InterviewBit](https://img.shields.io/badge/InterviewBit-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://www.interviewbit.com/profile/rattudacsit2021gate_d9a25bc44230/)


---

## 📊 **GitHub Stats & Metrics** 📊



![Profile Views](https://komarev.com/ghpvc/?username=Ratnesh-181998&color=blueviolet&style=for-the-badge&label=PROFILE+VIEWS)





<img src="https://github-readme-streak-stats.herokuapp.com/?user=Ratnesh-181998&theme=radical&hide_border=true&background=0D1117&stroke=4ECDC4&ring=F38181&fire=FF6B6B&currStreakLabel=4ECDC4" width="48%" />




<img src="https://github-readme-activity-graph.vercel.app/graph?username=Ratnesh-181998&theme=react-dark&hide_border=true&bg_color=0D1117&color=4ECDC4&line=F38181&point=FF6B6B" width="48%" />

---

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=4ECDC4&center=true&vCenter=true&width=600&lines=Ratnesh+Kumar+Singh;Data+Scientist+%7C+AI%2FML+Engineer;4%2B+Years+Building+Production+AI+Systems" alt="Typing SVG" />

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&duration=2000&pause=1000&color=F38181&center=true&vCenter=true&width=600&lines=Built+with+passion+for+the+AI+Community+🚀;Innovating+the+Future+of+AI+%26+ML;MLOps+%7C+LLMOps+%7C+AIOps+%7C+GenAI+%7C+AgenticAI+Excellence" alt="Footer Typing SVG" />


<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%">


