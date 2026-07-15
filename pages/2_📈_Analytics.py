
import streamlit as st
import plotly.express as px

from utils.data_loader import load_data

df = load_data()

st.title("📈 Restaurant Analytics")

st.write("Detailed insights about restaurants.")

st.subheader("📊 Dataset Summary")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Restaurants",
    len(df)
)

c2.metric(
    "Cities",
    df["City"].nunique()
)

c3.metric(
    "Countries",
    df["Country Code"].nunique()
)

c4.metric(
    "Average Rating",
    round(df["Aggregate rating"].mean(),2)
)

st.divider()

st.subheader("🍜 Top 10 Cuisines")

top = df["Cuisines"].value_counts().head(10)

fig = px.bar(
    x=top.values,
    y=top.index,
    orientation="h",
    color=top.values,
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig,use_container_width=True)

st.divider()

st.subheader("🏙️ Top Cities")

city = df["City"].value_counts().head(10)

fig = px.bar(
    x=city.index,
    y=city.values,
    color=city.values
)

st.plotly_chart(fig,use_container_width=True)

st.divider()

st.subheader("⭐ Rating Distribution")

fig = px.histogram(
    df,
    x="Aggregate rating",
    nbins=20,
    color_discrete_sequence=["green"]
)

st.plotly_chart(fig,use_container_width=True)

st.divider()

st.subheader("💰 Price Distribution")

fig = px.histogram(
    df,
    x="Price range",
    color_discrete_sequence=["orange"]
)

st.plotly_chart(fig,use_container_width=True)

st.divider()

st.subheader("🚚 Online Delivery")

delivery = df["Has Online delivery"].value_counts()

fig = px.pie(
    names=delivery.index,
    values=delivery.values,
    hole=.5
)

st.plotly_chart(fig,use_container_width=True)

st.divider()

st.subheader("👍 Votes vs Rating")

fig = px.scatter(
    df,
    x="Votes",
    y="Aggregate rating",
    color="Price range",
    hover_name="Restaurant Name"
)

st.plotly_chart(fig,use_container_width=True)

st.divider()

st.subheader("🍽️ Top Restaurant Chains")

chains = (
    df["Restaurant Name"]
    .value_counts()
    .head(15)
)

fig = px.bar(
    x=chains.index,
    y=chains.values,
    color=chains.values
)

st.plotly_chart(fig,use_container_width=True)