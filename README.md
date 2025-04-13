FloodMate: Your Personal Flood Safety Assistant

Stay safe. Stay connected. Stay ahead.

FloodMate is a mobile-first AI-powered web app that helps individuals and communities in Sarawak stay informed and prepared during flood emergencies. It combines real-time risk prediction, community-based reporting, and personal safety features in a single platform.

 🌧️ Core Features

- 🧠 AI Flood Risk Prediction 
  Predicts flood risk based on rainfall and river level inputs using a Random Forest machine learning model.

- 📩 Crowdsourced Flood Reporting 
  Allows community members to submit local flood conditions (location, water level, notes).

- 👨‍👩‍👧‍👦 Family Safety Tracker  
  Visual tracker panel to monitor the status of loved ones during emergencies.

- 📄 View Reports  
  Displays all submitted flood reports in a clean table.

- 🆘 Post-Flood Recovery Help  
  Quick links to insurance guidance, relief applications, and government support.


 ⚙️ How It Works

- Built with Streamlit for fast web app prototyping  
- AI Model trained in Google Colab using synthetic flood data  
- Uses `flood_model.pkl` to make real-time predictions in the app  
- Flood reports saved to `flood_reports.csv` (can be extended to database/API)


 📁 Project Structure

FloodMate/
├── app.py                  # Streamlit web app
├── flood_model.pkl         # Trained AI model
├── flood_reports.csv       # Saved user-submitted reports (auto-created)               
└── README.md               # Project documentation



 📊 Dataset

This project uses [synthetic flood data] generated based on global flood patterns and typical rainfall/river relationships in Southeast Asia. The structure simulates realistic inputs:

| rainfall_mm | river_level_m | flood_risk |
|-------------|----------------|------------|
| 30          | 2.1            | Low        |
| 90          | 3.9            | Medium     |
| 120         | 4.5            | High       |

> References:
> - [NASA EarthData](https://earthdata.nasa.gov)  
> - [Global Flood Database](https://www.globalfloods.eu)  
> - [Malaysia Open Data](https://www.data.gov.my)



 🚀 Project Flow

 Requirements
- Python 3.10+
- pip packages: `streamlit`, `pandas`, `scikit-learn`, `joblib`

 Install and Run
 --bash
pip install streamlit pandas scikit-learn joblib
streamlit run app.py



 🧠 Model Info
- Type: Random Forest Classifier  
- Input: Rainfall (mm), River Level (m)  
- Output: Flood Risk Category  
- Tool: Google Colab (training)



 💡 Future Plans
- Integrate with real-time data from MetMalaysia and JPS Sarawak  
- Add ESP32-based IoT sensor support  
- Expand user reporting to maps and photos  
- Deploy as native mobile app 



 👥 Team & Credits
- Fazrin Ezan – Project developer, AI model integration 
- ChatGPT (OpenAI) – Guidance and architecture 



 🌱 Built for:
AI for Resilient and Green Sarawak Hackathon 2025
> Empowering communities through real-time AI solutions
