
import streamlit as st
from utils.data_loader import load_data

from utils.export import download_csv
from utils.pdf_report import generate_pdf

# ---------------------------
# Load Dataset
# ---------------------------

df = load_data()

st.title("🔍 Restaurant Explorer")

st.write("Search restaurants and view detailed information.")

# ---------------------------
# Search Box
# ---------------------------

search = st.text_input(
    "Search Restaurant",
    placeholder="Example: Domino's"
)

# ---------------------------
# Search Logic
# ---------------------------

if search:

    result = df[
        df["Restaurant Name"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

    st.subheader("Search Results")

    if result.empty:

        st.error("❌ No matching restaurant found.")

        st.info("""
### Suggestions

✔ Check the restaurant name spelling.

✔ Try another restaurant.

✔ Search using a different keyword.

✔ Visit the Dashboard to explore available restaurants.
""")

    else:

        st.success(f"✅ {len(result)} Restaurant(s) Found")

        st.dataframe(result)

        restaurant = st.selectbox(
            "Select Restaurant",
            result["Restaurant Name"].unique()
        )

        details = result[
            result["Restaurant Name"] == restaurant
        ].iloc[0]

        st.subheader("Restaurant Details")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "⭐ Rating",
                details["Aggregate rating"]
            )

            st.metric(
                "👍 Votes",
                details["Votes"]
            )

            st.metric(
                "💰 Price Range",
                details["Price range"]
            )

        with col2:

            st.metric(
                "🍜 Cuisine",
                details["Cuisines"]
            )

            st.metric(
                "🚚 Online Delivery",
                details["Has Online delivery"]
            )

            st.metric(
                "🍽 Table Booking",
                details["Has Table booking"]
            )

        import plotly.express as px

        map_fig = px.scatter_mapbox(

            result[
                result["Restaurant Name"] == restaurant
            ],

            lat="Latitude",

            lon="Longitude",

            zoom=14,

            hover_name="Restaurant Name"

        )

        map_fig.update_layout(
            mapbox_style="open-street-map"
        )

        st.plotly_chart(
            map_fig,
            use_container_width=True
        )

        st.divider()

        st.subheader("📥 Export Results")

        col1, col2 = st.columns(2)

        with col1:
            download_csv(
                result,
                filename="Restaurant_Explorer.csv"
            )

        with col2:
            pdf = generate_pdf(result)

            with open(pdf, "rb") as file:

                st.download_button(

                    label="📄 Download PDF Report",

                    data=file,

                    file_name="Restaurant_Explorer_Report.pdf",

                    mime="application/pdf",

                    use_container_width=True

                )

else:

    st.info("🔍 Type a restaurant name to begin searching.")