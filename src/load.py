import pandas as pd


def load_dataset(path):
    df = pd.read_csv(path)

    df.loc[:, "DATE_TIME"] = pd.to_datetime(df["DATE_TIME"])
    df["HOUR"] = df["DATE_TIME"].apply(lambda _: _.hour)
    df["MONTH"] = df["DATE_TIME"].apply(lambda _: _.month)

    agg = df.groupby(["MONTH"]).agg({"AC_POWER": "sum", "DC_POWER": "sum"})

    agg["TOTAL_POWER"] = agg["AC_POWER"] + agg["DC_POWER"]

    return agg
