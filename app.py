import streamlit as st
from utils.ui import load_css

st.set_page_config(
    page_title="Restaurant Analytics Dashboard",
    page_icon="🍽️",
    layout="wide"
)

load_css()

st.markdown("""
<div style="
padding:25px;
border-radius:20px;
background:linear-gradient(90deg,#2563eb,#38bdf8);
color:white;
text-align:center;
">

<h1>🍽 Restaurant Analytics Dashboard</h1>

<p>
AI Powered Restaurant Analytics & Recommendation System
</p>

</div>
""",unsafe_allow_html=True)

st.title("🍽️ Restaurant Analytics Dashboard")

st.markdown("""
# Welcome 👋

This project is an **AI-Powered Restaurant Analytics Dashboard** developed using **Streamlit**.

### Available Modules

- 📊 Dashboard
- 📈 Analytics
- 🔍 Restaurant Explorer
- ⚖️ Restaurant Comparison
- 🤖 Restaurant Recommendation
- 🗺️ Restaurant Map

⬅️ Select any page from the sidebar.
""")

