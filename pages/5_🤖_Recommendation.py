
import streamlit as st

from utils.data_loader import load_data
from utils.recommendation import recommend_restaurants

from utils.export import download_csv
from utils.pdf_report import generate_pdf

df = load_data()

st.title("🤖 Restaurant Recommendation System")

st.write("Find the best restaurants based on your preferences.")

# City
cities = sorted(df["City"].dropna().unique())
city = st.selectbox("Select City", ["All"] + cities)

# Cuisine
cuisines = sorted(df["Cuisines"].dropna().unique())
cuisine = st.selectbox("Select Cuisine", ["All"] + cuisines)

# Budget
budget = st.selectbox(
    "Price Range",
    ["All", 1, 2, 3, 4]
)

# Rating
rating = st.slider(
    "Minimum Rating",
    0.0,
    5.0,
    4.0,
    0.1
)

if st.button("🍽 Recommend Restaurants"):

    recommendations = recommend_restaurants(
        df,
        city,
        cuisine,
        budget,
        rating
    )

    if recommendations.empty:
        st.warning("No matching restaurants found.")

    else:
        st.success(f"{len(recommendations)} Restaurants Found")

        st.dataframe(
            recommendations[
                [
                    "Restaurant Name",
                    "City",
                    "Cuisines",
                    "Aggregate rating",
                    "Votes",
                    "Average Cost for two",
                    "Price range"
                ]
            ]
        )


        st.divider()

        st.subheader("📥 Export Recommendations")

        col1, col2 = st.columns(2)

        with col1:
            download_csv(
                recommendations,
                filename="Recommended_Restaurants.csv"
            )

        with col2:
            pdf = generate_pdf(recommendations)

            with open(pdf, "rb") as file:
                st.download_button(
                    label="📄 Download PDF Report",
                    data=file,
                    file_name="Recommended_Restaurants_Report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )