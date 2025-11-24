# AI-Powered Fault Prediction in 5G Testbed

This project uses Machine Learning to predict upcoming 5G network faults using KPI (Key Performance Indicator) data.  
It includes:

- RandomForest ML model  
- Streamlit dashboard for real-time predictions  
- A synthetic 500-row 5G KPI dataset  
- End-to-end workflow for telecom fault detection  

---

## 🚀 Features
- Predicts *Normal* or *Fault Expected*
- Uses real-world KPIs:
  - Latency
  - Throughput
  - Jitter
  - Error Rate
  - CPU Usage
  - Memory Usage
  - Packet Loss
  - Handover Success Rate
- Real-time UI built using Streamlit

---

## 📂 Project Structure

5G-Fault-Prediction/ │-- model.py │-- dashboard.py │-- requirements.txt │-- README.md │-- .gitignore │-- (dataset + model files ignored from git)

---

## 🧠 How to Run the Project Locally

### 1) Clone the repo

git clone https://github.com/Shreshta7867/5G-Fault-Prediction.git cd 5G-Fault-Prediction

### 2) Create a virtual environment

python -m venv venv

### 3) Activate it
*PowerShell*

venv\Scripts\Activate.ps1

*CMD*

venv\Scripts\activate.bat

### 4) Install dependencies

pip install -r requirements.txt

### 5) Train the model

python model.py

### 6) Run the dashboard

streamlit run dashboard.py

---

## 💡 Tech Stack
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Joblib  

---

## 👥 Contributors
- Devi Sri Shreshta R 
- Chaitra Lakshmi Vardhan  

---

## 🔮 Future Improvements
- LSTM time-series fault prediction  
- Real 5G testbed integration  
- Cloud deployment  
- Explainable AI (SHAP)