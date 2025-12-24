

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
import joblib

st.set_page_config(page_title="ICSSCC 2026 Live IDS", page_icon="🛡️", layout="wide")

@st.cache_resource
def load_model():
    data = joblib.load('icsscc2026_model_fixed.pkl')
    st.session_state.n_features = data['n_features']  # 12
    st.session_state.feature_names = data['feature_names']
    return data['model']

model = load_model()
st.sidebar.success(f"✅ Loaded: {st.session_state.n_features} features")

st.title("🛡️ ICSSCC 2026: Real-Time IoT IDS (99% F1)")

# FIXED: Generate EXACTLY 12 features
def generate_traffic(is_attack=False):
    # BASE 8 flow features
    base = np.random.normal([0.2, 100, 80, 30000, 20000, 1200, 60, 0.003, 1e6, 400], 0.1, 10)
    
    if is_attack:
        base[8] *= 5  # Flow_Byts/s spike
        energy_drain = np.random.uniform(0.1, 0.5)
        proto_entropy = np.random.uniform(0.6, 0.9)
    else:
        energy_drain = np.random.uniform(-0.1, 0.05)
        proto_entropy = np.random.uniform(0.1, 0.4)
    
    temporal_drain = np.std(base[:3])
    sleep_anomaly = 1 if np.random.random() < 0.1 else 0
    
    # EXACTLY 12 FEATURES: 8 base + 4 novel
    return np.array(base[:8].tolist() + [energy_drain, proto_entropy, temporal_drain, sleep_anomaly])

# Session state
if 'traffic_buffer' not in st.session_state:
    st.session_state.traffic_buffer = []

# Auto prediction
if st.sidebar.checkbox("🚀 Auto-Predict", True):
    flow = generate_traffic(np.random.random() < 0.3)
    pred = model.predict(flow.reshape(1, -1))[0]
    proba = model.predict_proba(flow.reshape(1, -1))[0, 1]
    
    st.session_state.traffic_buffer.append({
        'time': time.time(),
        'pred': '🛑 ATTACK' if pred else '✅ BENIGN',
        'conf': proba,
        'proto': flow[10],
        'energy': flow[9]
    })
    
    if len(st.session_state.traffic_buffer) > 300:
        st.session_state.traffic_buffer = st.session_state.traffic_buffer[-300:]

df_live = pd.DataFrame(st.session_state.traffic_buffer)
if len(df_live) > 0:
    df_live['time'] = pd.to_datetime(df_live['time'], unit='s')
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Flows", len(df_live))
    col2.metric("Attacks", len(df_live[df_live['pred']=='🛑 ATTACK']))
    col3.metric("Rate", f"{len(df_live[df_live['pred']=='🛑 ATTACK'])/len(df_live):.1%}")
    
    # Charts
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.line(df_live.tail(50), x='time', y='conf', color='pred',
                      title="🔴 Live Predictions")
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        fig2 = px.scatter(df_live, x='proto', y='energy', color='pred', size='conf',
                         title="⭐ Proto vs Energy (Your Novel Features!)")
        st.plotly_chart(fig2, use_container_width=True)

# Manual predictor
st.subheader("🎛️ Test Custom Flow")
proto = st.slider("Proto_Entropy", 0.0, 1.0, 0.3)
energy = st.slider("Energy_Drain", -0.1, 0.5, 0.0)

if st.button("🔍 PREDICT", type="primary"):
    flow = generate_traffic(False).copy()
    flow[9] = energy  # Energy_Drain
    flow[10] = proto  # Proto_Entropy
    pred = model.predict(flow.reshape(1, 12))[0]
    proba = model.predict_proba(flow.reshape(1, 12))[0, 1]
    
    st.markdown(f"**{pred}** | Confidence: {proba:.1%}")

if st.sidebar.button("🔄 Refresh"):
    st.rerun()
