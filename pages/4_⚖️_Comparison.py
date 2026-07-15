
import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("⚖️ Restaurant Comparison")

restaurant_names = sorted(df["Restaurant Name"].dropna().unique())

col1, col2 = st.columns(2)

with col1:
    restaurant1 = st.selectbox(
        "Select Restaurant 1",
        restaurant_names
    )

with col2:
    restaurant2 = st.selectbox(
        "Select Restaurant 2",
        restaurant_names,
        index=1
    )

r1 = df[df["Restaurant Name"] == restaurant1].iloc[0]
r2 = df[df["Restaurant Name"] == restaurant2].iloc[0]

comparison = pd.DataFrame({

    "Feature":[
        "City",
        "Cuisine",
        "Rating",
        "Votes",
        "Average Cost",
        "Price Range",
        "Online Delivery",
        "Table Booking"
    ],

    restaurant1:[
        r1["City"],
        r1["Cuisines"],
        r1["Aggregate rating"],
        r1["Votes"],
        r1["Average Cost for two"],
        r1["Price range"],
        r1["Has Online delivery"],
        r1["Has Table booking"]
    ],

    restaurant2:[
        r2["City"],
        r2["Cuisines"],
        r2["Aggregate rating"],
        r2["Votes"],
        r2["Average Cost for two"],
        r2["Price range"],
        r2["Has Online delivery"],
        r2["Has Table booking"]
    ]

})

st.subheader("Comparison Table")

st.dataframe(
    comparison,
    use_container_width=True
)

rating_df = pd.DataFrame({

    "Restaurant":[restaurant1,restaurant2],

    "Rating":[
        r1["Aggregate rating"],
        r2["Aggregate rating"]
    ]

})

fig = px.bar(

    rating_df,

    x="Restaurant",

    y="Rating",

    title="Restaurant Rating Comparison",

    color="Restaurant"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

votes_df = pd.DataFrame({

    "Restaurant":[restaurant1,restaurant2],

    "Votes":[
        r1["Votes"],
        r2["Votes"]
    ]

})

fig = px.bar(

    votes_df,

    x="Restaurant",

    y="Votes",

    title="Votes Comparison",

    color="Restaurant"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

cost_df = pd.DataFrame({

    "Restaurant":[restaurant1,restaurant2],

    "Cost":[
        r1["Average Cost for two"],
        r2["Average Cost for two"]
    ]

})

fig = px.bar(

    cost_df,

    x="Restaurant",

    y="Cost",

    title="Average Cost Comparison",

    color="Restaurant"

)

st.plotly_chart(
    fig,
    use_container_width=True
)


map_df = pd.DataFrame({

    "Restaurant":[restaurant1,restaurant2],

    "Latitude":[
        r1["Latitude"],
        r2["Latitude"]
    ],

    "Longitude":[
        r1["Longitude"],
        r2["Longitude"]
    ]

})

fig = px.scatter_mapbox(

    map_df,

    lat="Latitude",

    lon="Longitude",

    hover_name="Restaurant",

    zoom=3,

    height=500

)

fig.update_layout(

    mapbox_style="open-street-map",

    margin=dict(l=0,r=0,t=0,b=0)

)

st.plotly_chart(
    fig,
    use_container_width=True
)