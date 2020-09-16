# This file is based on: https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/app.py

"""An example of showing geographic data."""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

DATE_TIME = "date/time"
DATA_URL = (
    "http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)
TOTAL_SAMPLES = 100000

st.title("Uber Pickups in New York City")
st.markdown(
    """
This is a demo of a Streamlit app that shows the Uber pickups
geographical distribution in New York City. Use the slider
to pick a specific hour and look at how the charts change.

[See source code](https://github.com/streamlit/demo-uber-nyc-pickups/blob/master/app.py)
"""
)


@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename(lambda x: str(x).lower(), axis="columns", inplace=True)
    data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data


def run():
    data = load_data(TOTAL_SAMPLES)

    hour = st.slider("Hour to look at", 0, 23)

    data = data[data[DATE_TIME].dt.hour == hour]

    st.subheader("Geo data between %i:00 and %i:00" % (hour, (hour + 1) % 24))
    midpoint = (np.average(data["lat"]), np.average(data["lon"]))

    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": midpoint[0],
                "longitude": midpoint[1],
                "zoom": 11,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=data,
                    get_position=["lon", "lat"],
                    radius=100,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
            ],
        )
    )

    st.subheader(
        "Breakdown by minute between %i:00 and %i:00" % (hour, (hour + 1) % 24)
    )
    filtered = data[
        (data[DATE_TIME].dt.hour >= hour) & (data[DATE_TIME].dt.hour < (hour + 1))
    ]
    hist = np.histogram(filtered[DATE_TIME].dt.minute, bins=60, range=(0, 60))[0]
    chart_data = pd.DataFrame({"minute": range(60), "pickups": hist})

    st.altair_chart(
        alt.Chart(chart_data)
        .mark_area(
            interpolate="step-after",
        )
        .encode(
            x=alt.X("minute:Q", scale=alt.Scale(nice=False)),
            y=alt.Y("pickups:Q"),
            tooltip=["minute", "pickups"],
        ),
        use_container_width=True,
    )

    if st.checkbox("Show raw data", False):
        st.subheader(
            "Raw data by minute between %i:00 and %i:00" % (hour, (hour + 1) % 24)
        )
        st.write(data)


if __name__ == "__main__":
    run()
