
import streamlit as st
from utils.data_loader import load_data
from utils.filters import sidebar_filters
from utils.export import download_csv
from utils.pdf_report import generate_pdf
from utils.charts import (
    rating_distribution,
    price_distribution,
    top_cities,
    top_cuisines,
    restaurant_map
)


# Load Dataset
df = load_data()
selected_city, selected_cuisine, selected_price, selected_rating = sidebar_filters(df)

st.title("📊 Dashboard")

st.write("Overview of Restaurant Dataset")

filtered_df = df.copy()

# City
if selected_city != "All":
    filtered_df = filtered_df[
        filtered_df["City"] == selected_city
    ]

# Cuisine
if selected_cuisine != "All":
    filtered_df = filtered_df[
        filtered_df["Cuisines"] == selected_cuisine
    ]

# Price
if selected_price != "All":
    filtered_df = filtered_df[
        filtered_df["Price range"] == selected_price
    ]

# Rating
filtered_df = filtered_df[
    filtered_df["Aggregate rating"] >= selected_rating
]

# ======================
# KPI Cards
# ======================

total_restaurants = len(filtered_df)

avg_rating = round(filtered_df["Aggregate rating"].mean(),2) if not filtered_df.empty else 0

avg_votes = round(filtered_df["Votes"].mean(),2) if not filtered_df.empty else 0

avg_cost = round(filtered_df["Average Cost for two"].mean(),2) if not filtered_df.empty else 0

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Restaurants",
    total_restaurants
)

col2.metric(
    "Average Rating",
    avg_rating
)

col3.metric(
    "Average Votes",
    avg_votes
)

col4.metric(
    "Average Cost",
    avg_cost
)

st.divider()

st.subheader("Dataset Preview")

if filtered_df.empty:
    st.warning("No restaurants found. Try changing the filters.")
else:
    st.dataframe(filtered_df)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        rating_distribution(filtered_df)

    with col2:
        price_distribution(filtered_df)

    st.divider()

    col3, col4 = st.columns(2)

    with col3:
        top_cities(filtered_df)

    with col4:
        top_cuisines(filtered_df)

st.divider()
restaurant_map(filtered_df)

download_csv(filtered_df)

pdf = generate_pdf(filtered_df)

with open(pdf, "rb") as file:

    st.download_button(

        label="📄 Download PDF Report",

        data=file,

        file_name="Restaurant_Analytics_Report.pdf",

        mime="application/pdf",

        use_container_width=True

    )
   