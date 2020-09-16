import altair as alt
import streamlit as st

from src.load import load_dataset


def app():
    """Run the demo app."""

    st.title("Solar Energy Output :sunny:")

    plant = st.selectbox("Select Plant", ["Plant 1", "Plant 2"])

    total_yield = load_dataset(f"data/{plant.lower().replace(' ', '-')}.csv.zip")

    chart = (
        alt.Chart(total_yield.reset_index())
        .mark_bar()
        .encode(
            x=alt.X("MONTH", type="ordinal", title="Month"),
            y=alt.Y("TOTAL_POWER", title="Power (kW)"),
            tooltip=["TOTAL_POWER"],
        )
    )

    st.altair_chart(chart, use_container_width=True)

    st.dataframe(total_yield.reset_index())


if __name__ == "__main__":
    app()
