import streamlit as st
import plotly.express as px


# ----------------------------
# Rating Distribution
# ----------------------------

def rating_distribution(df):

    st.subheader("⭐ Rating Distribution")

    fig = px.histogram(
        df,
        x="Aggregate rating",
        nbins=20,
        title="Distribution of Restaurant Ratings",
        color_discrete_sequence=["royalblue"]
    )

    fig.update_layout(
        xaxis_title="Rating",
        yaxis_title="Restaurants"
    )

    st.plotly_chart(fig, use_container_width=True)


# ----------------------------
# Price Distribution
# ----------------------------

def price_distribution(df):

    st.subheader("💰 Price Range Distribution")

    price = df["Price range"].value_counts().sort_index()

    fig = px.bar(
        x=price.index,
        y=price.values,
        labels={
            "x":"Price Range",
            "y":"Restaurants"
        },
        color=price.values,
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig, use_container_width=True)


# ----------------------------
# Top Cities
# ----------------------------

def top_cities(df):

    st.subheader("🏙️ Top Cities")

    city = (
        df["City"]
        .value_counts()
        .head(10)
    )

    fig = px.bar(
        x=city.values,
        y=city.index,
        orientation="h",
        labels={
            "x":"Restaurants",
            "y":"City"
        },
        color=city.values,
        color_continuous_scale="Greens"
    )

    st.plotly_chart(fig, use_container_width=True)


# ----------------------------
# Top Cuisines
# ----------------------------

def top_cuisines(df):

    st.subheader("🍜 Top Cuisines")

    cuisine = (
        df["Cuisines"]
        .value_counts()
        .head(10)
    )

    fig = px.bar(
        x=cuisine.values,
        y=cuisine.index,
        orientation="h",
        labels={
            "x":"Restaurants",
            "y":"Cuisine"
        },
        color=cuisine.values,
        color_continuous_scale="Oranges"
    )

    st.plotly_chart(fig, use_container_width=True)


import plotly.express as px
import streamlit as st

# ----------------------------------
# Restaurant Map
# ----------------------------------

def restaurant_map(df):

    st.subheader("📍 Restaurant Locations")

    map_df = df.dropna(subset=["Latitude", "Longitude"])

    fig = px.scatter_mapbox(
        map_df,
        lat="Latitude",
        lon="Longitude",
        hover_name="Restaurant Name",
        hover_data=[
            "Aggregate rating",
            "Votes",
            "City"
        ],
        zoom=3,
        height=600
    )

    fig.update_layout(
        mapbox_style="open-street-map",
        margin=dict(l=0, r=0, t=0, b=0)
    )

    st.plotly_chart(fig, use_container_width=True)