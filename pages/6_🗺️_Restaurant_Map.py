
import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("🗺 Restaurant Map")

st.write("Explore restaurant locations interactively.")

st.sidebar.header("📍 Map Filters")

# City
cities = sorted(df["City"].dropna().unique())

selected_city = st.sidebar.selectbox(
    "City",
    ["All"] + cities
)

# Cuisine
cuisines = sorted(df["Cuisines"].dropna().unique())

selected_cuisine = st.sidebar.selectbox(
    "Cuisine",
    ["All"] + cuisines
)

# Price Range
selected_price = st.sidebar.selectbox(
    "Price Range",
    ["All",1,2,3,4]
)

# Rating
selected_rating = st.sidebar.slider(
    "Minimum Rating",
    0.0,
    5.0,
    3.0,
    0.1
)

filtered_df = df.copy()

if selected_city != "All":
    filtered_df = filtered_df[
        filtered_df["City"] == selected_city
    ]

if selected_cuisine != "All":
    filtered_df = filtered_df[
        filtered_df["Cuisines"].str.contains(
            selected_cuisine,
            case=False,
            na=False
        )
    ]

if selected_price != "All":
    filtered_df = filtered_df[
        filtered_df["Price range"] == selected_price
    ]

filtered_df = filtered_df[
    filtered_df["Aggregate rating"] >= selected_rating
]

st.subheader("📊 Map Statistics")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Restaurants",
    len(filtered_df)
)

c2.metric(
    "Average Rating",
    round(filtered_df["Aggregate rating"].mean(),2)
)

c3.metric(
    "Average Votes",
    round(filtered_df["Votes"].mean(),2)
)

c4.metric(
    "Average Cost",
    round(filtered_df["Average Cost for two"].mean(),2)
)

st.divider()

st.subheader("🌍 Restaurant Locations")

map_df = filtered_df.dropna(
    subset=["Latitude","Longitude"]
)

fig = px.scatter_mapbox(

    map_df,

    lat="Latitude",

    lon="Longitude",

    hover_name="Restaurant Name",

    hover_data=[

        "City",

        "Cuisines",

        "Aggregate rating",

        "Votes"

    ],

    color="Aggregate rating",

    size="Votes",

    zoom=3,

    height=700

)

fig.update_layout(

    mapbox_style="open-street-map",

    margin=dict(
        l=0,
        r=0,
        t=0,
        b=0
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("📋 Restaurants")

st.dataframe(

    filtered_df[

        [

            "Restaurant Name",

            "City",

            "Cuisines",

            "Aggregate rating",

            "Votes",

            "Average Cost for two"

        ]

    ],

    use_container_width=True

)