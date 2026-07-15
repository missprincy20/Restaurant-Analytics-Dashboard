import pandas as pd

def recommend_restaurants(df, city, cuisine, budget, rating):

    result = df.copy()

    # City Filter
    if city != "All":
        result = result[result["City"] == city]

    # Cuisine Filter
    if cuisine != "All":
        result = result[
            result["Cuisines"].str.contains(
                cuisine,
                case=False,
                na=False
            )
        ]

    # Budget Filter
    if budget != "All":
        result = result[result["Price range"] == budget]

    # Rating Filter
    result = result[
        result["Aggregate rating"] >= rating
    ]

    # Sort Results
    result = result.sort_values(
        by=["Aggregate rating", "Votes"],
        ascending=False
    )

    return result.head(10)