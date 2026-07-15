import streamlit as st

def sidebar_filters(df):

    st.sidebar.header("🔍 Filters")

    # City Filter
    cities = sorted(df["City"].dropna().unique())

    selected_city = st.sidebar.selectbox(
        "Select City",
        ["All"] + cities
    )

    # Cuisine Filter
    cuisines = sorted(df["Cuisines"].dropna().unique())

    selected_cuisine = st.sidebar.selectbox(
        "Select Cuisine",
        ["All"] + cuisines
    )

    # Price Range
    prices = sorted(df["Price range"].dropna().unique())

    selected_price = st.sidebar.selectbox(
        "Price Range",
        ["All"] + list(prices)
    )

    # Rating
    selected_rating = st.sidebar.slider(
        "Minimum Rating",
        0.0,
        5.0,
        3.0,
        0.1
    )

    return (
        selected_city,
        selected_cuisine,
        selected_price,
        selected_rating
    )