import pandas as pd
import seaborn as sns
import altair as alt


def main():
    asec = pd.read_pickle("ipums/asec.pkl")

    # Filtering
    asec = asec[asec["WORKLY"] == 2]  # worked last year
    asec = asec[asec["FULLPART"] == 1]  # fulltime
    asec = asec[asec["UHRSWORKLY"] >= 35]  # work at least 35 hours

    # Adjust inflation to 2022 dollars
    asec["INCWAGE_U"] = asec["INCWAGE"] * asec["CPI99"] * 1.797

    # Calculate hourly wage based on adjusted wage
    asec["HOURLYWAGE"] = asec["INCWAGE_U"] / (asec["WKSWORK1"] * asec["UHRSWORKLY"])

    # Replace gender labels
    asec["SEX"] = asec["SEX"].astype(str).replace({"1": "Male", "2": "Female"})

    # Gender wage gap
    gender_wages = (
        asec.groupby(["YEAR", "SEX"])["HOURLYWAGE"]
        .apply(lambda x: x.quantile([0.15, 0.5, 0.9]))
        .unstack()
        .reset_index()
    )
    gender_wages.columns = ["YEAR", "SEX", "15th", "50th", "90th"]

    alt.Chart(median_wages).mark_line(point=True).encode(
        x="YEAR:O",
        y="HOURLYWAGE:Q",
        color="SEX:N",
    )


if __name__ == "__main__":
    main()
