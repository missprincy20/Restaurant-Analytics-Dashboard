import streamlit as st


def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


# ===========================
# Custom KPI Card
# ===========================

def metric_card(title, value, emoji):

    html = f"""
<div class="metric-card">
    <div class="metric-title">{emoji} {title}</div>
    <div class="metric-value">{value}</div>
</div>
"""

    st.markdown(html, unsafe_allow_html=True)