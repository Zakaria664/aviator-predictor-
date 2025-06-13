# ---

### ✍🏽 To Edit in VS Code:
1. Open the `README.md` file.
2. Fix the line manually by:
   - Giving a proper title with `#`
      - Wrapping code in triple backticks (```python ... ```)
      
      Let me know if you'd like me to generate a full cleaned-up `README.md` for your project!# ✈️ Aviator Predictor
      
      **Aviator Predictor** is a web-based application designed to help players track, analyze, and predict trends in the Aviator betting game using historical data visualization and simple AI logic.
      
      ---
      
      ## 📱 Screenshot Preview
      
      | Login Screen | Dashboard | Graph Analytics |
      |--------------|-----------|-----------------|
      | ![Login](https://via.placeholder.com/250x500.png?text=Login+Screen) | ![Dashboard](https://via.placeholder.com/250x500.png?text=Dashboard) | ![Graph](https://via.placeholder.com/250x500.png?text=Graph+Analytics) |
      
      ---
      
      ## ⚙️ Features
      
      - 📈 Real-time graph trends
      - 🧠 Bet prediction logic (basic AI)
      - 🔐 User authentication
      - 📊 Historical logs & statistics
      - 💾 Export/Download CSV logs
      - 📱 Mobile-optimized layout
      
      ---
      
      ## 🚀 Installation
      
      ```bash
      git clone https://github.com/Zakaria664/aviator-predictor.git
      cd aviator-predictor
      python aviator_app.pyaviator-predictor-import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# Page configuration
st.set_page_config(
    page_title="Aviator Predictor by Sakarea Mothwe",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
    }
    h1, h2, h3 {
        color: #003366;
    }
    .stButton>button {
        background-color: #003366;
        color: white;
        font-weight: bold;
    }
    .stDataFrame {
        border: 2px solid #003366;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🛩️ Aviator Predictor")
st.subheader("Smart Betting Companion by Sakarea Mothwe")

st.markdown("""
Welcome to the Aviator Predictor app — your intelligent tool for analyzing historical multipliers to guide future betting strategies. 

Track your bets, visualize trends, and make informed decisions.
""")

# --- Section: User Betting Input & Tracker ---
st.header("📊 Bet Tracker")

if "bet_log" not in st.session_state:
    st.session_state["bet_log"] = []

with st.form("bet_input"):
    multiplier = st.number_input("Enter Last Game Multiplier (e.g. 1.87):", min_value=0.01, step=0.01, format="%.2f")
    stake = st.number_input("Bet Amount (Optional):", min_value=0.0, step=0.5, format="%.2f")
    time = st.time_input("Game Time", value=datetime.datetime.now().time())
    log_bet = st.form_submit_button("Log Bet")
    
    if log_bet:
        st.session_state["bet_log"].append({
            "Time": time.strftime("%H:%M:%S"),
            "Multiplier": multiplier,
            "Stake": stake,
        })
        st.success("✅ Bet logged successfully.")

# Show logged data
if st.session_state["bet_log"]:
    df = pd.DataFrame(st.session_state["bet_log"])
    st.dataframe(df)

    # Save to CSV
    if st.download_button("Download History as CSV", df.to_csv(index=False), file_name="aviator_bet_history.csv"):
        st.success("🗂️ Download ready.")

# --- Section: History Analytics ---
st.header("📈 History Analytics")

if st.session_state["bet_log"]:
    multipliers = df["Multiplier"]
    mean_val = multipliers.mean()
    std_dev = multipliers.std()
    count = len(multipliers)

    st.markdown(f"""
    **🔍 Summary Stats:**
    - Number of Records: `{count}`
    - Average Multiplier: `{mean_val:.2f}`
    - Standard Deviation: `{std_dev:.2f}`
    """)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df["Multiplier"], marker='o', linestyle='--', color='green')
    ax.axhline(mean_val, color='blue', linestyle='-', label='Average')
    ax.set_title("Multiplier Trend Over Time")
    ax.set_ylabel("Multiplier")
    ax.set_xlabel("Entry Index")
    ax.legend()
    st.pyplot(fig)

# --- Section: Guidelines ---
st.sidebar.title("📘 Betting Guidelines")
st.sidebar.markdown("""
Use this tool to identify patterns in multiplier behaviors.

🧠 **Smart Betting Tips:**
- Avoid chasing after extreme highs.
- Bet after observing a dip or consistent streak of low multipliers.
- Don’t rely solely on the app — combine with experience.
- Set a **limit** and stick to your budget!

*Created by Sakarea Mothwe, RN – Botswana*
""")

# Footer
st.markdown("""
---
App designed by **Sakarea Mothwe** | 📍 Botswana  
Specialist in **Emergency & Occupational Health Nursing**  
""")
