import pandas as pd
import base64
import numpy as np
from io import BytesIO
from app.utils import scrape_wikipedia_table
from app.plotting import run_plot

async def process_task(questions_file, attachments):
    questions = (await questions_file.read()).decode()
    files = {file.filename: await file.read() for file in attachments}

    if "wikipedia" in questions.lower():
        url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"
        df = scrape_wikipedia_table(url)

        df["Worldwide gross"] = (df["Worldwide gross"].replace('[\$,]', '', regex=True).apply(lambda x: pd.to_numeric(x, errors='coerce')))
        # Optional: Drop rows with invalid (non-numeric) values
        df = df.dropna(subset=["Worldwide gross"])

        df["Rank"] = df["Rank"].astype(int)
        df["Peak"] = df["Peak"].astype(int)

        q1 = len(df[(df["Worldwide gross"] >= 2_000_000_000) & (df["Year"] < 2000)])
        q2 = df[df["Worldwide gross"] >= 1_500_000_000].sort_values("Year").iloc[0]["Title"]
        q3 = round(df["Rank"].corr(df["Peak"]), 6)
        plot = run_plot(df)

        return [q1, q2, q3, plot]

    return ["Unknown", "Unknown", 0.0, ""]
