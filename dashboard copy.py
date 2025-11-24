import streamlit as st
import joblib
import numpy as np

# Load ML model
model = joblib.load("fault_model.pkl")

st.title("AI-Powered 5G Fault Prediction System")

st.write("Enter the 5G KPI values below:")

latency = st.number_input("Latency (ms)", 0.0, 200.0, 20.0)
throughput = st.number_input("Throughput (Mbps)", 0.0, 200.0, 100.0)
jitter = st.number_input("Jitter (ms)", 0.0, 50.0, 2.0)
error_rate = st.number_input("Error Rate", 0.0, 1.0, 0.005)
cpu = st.number_input("CPU Usage (%)", 0.0, 100.0, 40.0)
memory = st.number_input("Memory Usage (%)", 0.0, 100.0, 50.0)
handover = st.number_input("Handover Success Rate", 0.0, 1.0, 0.98)
packet_loss = st.number_input("Packet Loss", 0.0, 1.0, 0.002)

if st.button("Predict Fault"):
    values = np.array([[latency, throughput, jitter, error_rate, cpu, memory, handover, packet_loss]])
    result = model.predict(values)[0]

    if result == 1:
        st.error("⚠ Fault Expected")
    else:
        st.success("✔ No Fault Detected")
