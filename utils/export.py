import pandas as pd
import streamlit as st

def download_csv(df, filename="filtered_restaurants.csv"):
    """
    Download dataframe as CSV
    """

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name=filename,
        mime="text/csv",
        use_container_width=True
    )