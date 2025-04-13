# FloodMate: Your Personal Flood Safety Assistant

import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="FloodMate", page_icon="🌊")

# Load AI model
model = joblib.load("flood_model.pkl")

st.title("🌊 FloodMate: Your Personal Flood Safety Assistant")
st.markdown("Stay safe. Stay connected. Stay ahead.")

# --- Section 1: Flood Risk Prediction ---
st.header("🧠 AI-Powered Flood Risk Prediction")

rainfall = st.number_input("Rainfall (in mm)", min_value=0.0, max_value=300.0, value=50.0)
river_level = st.number_input("River Level (in meters)", min_value=0.0, max_value=10.0, value=2.5)

if st.button("Predict Flood Risk"):
    input_df = pd.DataFrame([[rainfall, river_level]], columns=["rainfall_mm", "river_level_m"])
    prediction = model.predict(input_df)

    # Adjust label_map if needed (depends on label encoder order)
    label_map = {0: "High", 1: "Low", 2: "Medium"}
    risk_label = label_map.get(prediction[0], "Unknown")

    st.success(f"Predicted Flood Risk: {risk_label}")

st.divider()

# --- Section 2: Community Flood Report ---
st.header("📩 Report a Flood in Your Area")

with st.form("flood_report_form"):
    name = st.text_input("Your Name")
    location = st.text_input("Location / Street Name")
    level = st.slider("Approximate Water Level (cm)", 0, 200, 10)
    note = st.text_area("Additional Notes (optional)")
    submit = st.form_submit_button("Submit Report")

    if submit:
        report_df = pd.DataFrame([[name, location, level, note]], columns=["Name", "Location", "WaterLevel(cm)", "Note"])
        report_file = "flood_reports.csv"
        if os.path.exists(report_file):
            existing = pd.read_csv(report_file)
            report_df = pd.concat([existing, report_df], ignore_index=True)
        report_df.to_csv(report_file, index=False)
        st.success("✅ Thank you! Your flood report has been recorded.")

# --- Section 2.5: View Submitted Reports ---
if os.path.exists("flood_reports.csv"):
    st.subheader("📄 Submitted Flood Reports")
    submitted_df = pd.read_csv("flood_reports.csv")
    st.dataframe(submitted_df, use_container_width=True)

st.divider()

# --- Section 3: Family Safety Tracker ---
st.header("👨‍👩‍👧‍👦 Family Safety Tracker")

st.markdown("""
- 👤 **Ali** – ✅ Safe  
- 👤 **Nabila** – ❗ In danger zone  
- 👤 **Amira** – ✅ Safe  
- 👤 **Zul** – ❗ Last location: Pending update  
""")

st.divider()

# --- Section 4: Post-Flood Recovery Help ---
st.header("🆘 Post-Flood Recovery Assistant")

st.markdown("""
If you're affected by flooding, here are resources to help:

- 📞 **Emergency Hotline:** 999 or local disaster relief line  
- 📝 [Apply for Relief Aid (Google Form)](https://forms.gle/example)  
- 💬 [Contact Local Authority Support Center](https://sarawak.gov.my)  
- 📄 [How to Claim Flood Insurance (PDF)](https://example.com/flood-insurance-guide.pdf)
""")

st.divider()
st.markdown("✅ *Model trained using synthetic data with Random Forest classifier*")

