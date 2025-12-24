#  Real-Time IoT Intrusion Detection Dashboard

**99% F1-Score | 0.9992 ROC-AUC | Novel Sustainable Features | Live Predictions**

streamlit link : https://iot-dashboard-sustainablemodel.streamlit.app/

##  Project Overview

Real-time dashboard for IoT network intrusion detection using XGBoost with **4 novel sustainable features**:

- **Protocol Entropy Flux** (MITM detection, importance=0.573) 
- **Energy Drain Score** (DoS battery physics)
- **Temporal Drift Vector** (botnet evolution)
- **Sleep Anomaly** (low-power evasion)

**Dataset:** IoTID20 (Wi-Fi camera traffic: Mirai, SYN flood, ARP spoofing)

##  Performance
| Metric     | Score    |
|------------|----------|
| **F1-Score** | **99.0%** |
| **ROC-AUC**  | **0.9992** |
| **Accuracy** | **99.0%** |

##  Quick Start

### 1. Clone & Install
git clone https://github.com/srinidhi2006/IoT-Dashboard<br>
cd iot-ids-dashboard<br>
pip install -r requirements.txt<br>

### 2. Run Dashboard
streamlit run app.py<br>
**URL:** http://localhost:8501

##  Files
├── app.py # Main dashboard (single file!)<br>
├── requirements.txt # Dependencies<br>
└── README.md # This file<br>

##  Live Features

-  **Real-time predictions** (1/sec auto)
-  **Live attack rate** & confidence metrics
-  **Novel features scatter plot** (Proto_Entropy vs Energy_Drain)
-  **Manual attack simulator** (sliders)
-  **Recent predictions table**
-  **Mobile responsive**

##  Usage Examples

### Auto Mode (Live Traffic)
Enable "Auto Predict"<br>
Watch 30% attack simulation<br>
Red dots = BLOCKED attacks!<br>

## 🔧 Feature Importance

Proto_Entropy → 57.3% <br>
Flow_Byts/s → 15.0%<br>
Flow_Duration → 12.0%<br>
Energy_Drain → 2.1%<br>
Temporal_Drift → 2.1%<br>
Sleep_Anomaly → 0.2%<br>

## 🌐 Deployment Options

### Streamlit Cloud (FREE)

Push to GitHub<br>
share.streamlit.io → Deploy<br>

## 📦 Requirements
streamlit==1.38.0<br>
plotly==5.24.1<br>
xgboost==2.1.1<br>
pandas==2.2.3<br>
numpy==2.1.1<br>
joblib==1.4.2<br>
scikit-learn==1.5.2<br>

## 🔍 Technical Details

**Model:** XGBoost (200 trees, max_depth=6)  
**Features:** 12 total (8 CICFlowMeter + 4 novel)  
**Dataset:** IoTID20 (~600K flows, balanced)  
**Inference:** <1ms per prediction  
**Memory:** <500MB RAM  

## 🤝 Contributing
Fork repository<br>
Create feature branch<br>
Commit changes<br>
Push <br>


## 📄 License
MIT License - Free for commercial & research use.

## 👨‍💻 Author
**Sri Nidhi**  
 

## 🙏 Acknowledgments
- IoTID20 Dataset Team
- Streamlit Community
- XGBoost Contributors
- CICFlowMeter

---

**Star if useful!**  |  **Issues welcome!** 
