from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os

def generate_pdf(df):

    filename = "Restaurant_Analytics_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    # ----------------------
    # Title
    # ----------------------

    story.append(
        Paragraph("<b>Restaurant Analytics Report</b>", styles["Title"])
    )

    story.append(Spacer(1,20))

    # ----------------------
    # Date
    # ----------------------

    story.append(
        Paragraph(
            f"Generated On : {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,20))

    # ----------------------
    # KPI
    # ----------------------

    story.append(
        Paragraph(f"Total Restaurants : {len(df)}", styles["Heading2"])
    )

    story.append(
        Paragraph(
            f"Average Rating : {round(df['Aggregate rating'].mean(),2)}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Average Votes : {round(df['Votes'].mean(),2)}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Average Cost for Two : {round(df['Average Cost for two'].mean(),2)}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,20))

    # ----------------------
    # Top Cities
    # ----------------------

    story.append(
        Paragraph("<b>Top 5 Cities</b>", styles["Heading2"])
    )

    top_cities = df["City"].value_counts().head(5)

    for city, count in top_cities.items():

        story.append(
            Paragraph(
                f"{city} : {count}",
                styles["Normal"]
            )
        )

    story.append(Spacer(1,20))

    # ----------------------
    # Top Cuisines
    # ----------------------

    story.append(
        Paragraph("<b>Top 5 Cuisines</b>", styles["Heading2"])
    )

    top_cuisines = df["Cuisines"].value_counts().head(5)

    for cuisine, count in top_cuisines.items():

        story.append(
            Paragraph(
                f"{cuisine} : {count}",
                styles["Normal"]
            )
        )

    doc.build(story)

    return filename