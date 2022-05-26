#from turtle import title
import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv("/Users/maris/Documents/Programming/nonlinear-dashboard/podcasts-2015-05-01_to_2022-05-05.csv")#[2500:]
df["date"] = pd.to_datetime(df["date"])
df = df.loc[(df['date'] > '2021-10-12')].reset_index(drop=True)

df2 = pd.read_csv("/Users/maris/Documents/Programming/nonlinear-dashboard/Plays 20190601-20220506.csv")
df2["date"] = pd.to_datetime(df2["Pacific Time"])
print(len(df2))
df2 = df2[df2["Minutes played"] > 1]
print(len(df2))
df2.index = pd.DatetimeIndex(df2.date)
idx = pd.date_range("2021-10-13", "2022-05-06")
df2 = df2.reindex(idx, fill_value=0).drop(["date"], axis=1)
df2 = df2.rename_axis('date').reset_index()
df2["date"] = pd.to_datetime(df2["date"])
df2 = df2.astype({"Pacific Time": str})
print(df2)

df0 = pd.merge(df, df2, on="date").reset_index(drop=True)
df0 = df0.fillna(0)
df0["streams_plays"] = df0["streams"] + df0["Plays"]

st.title("Nonlinear Library Analytics")

c = alt.Chart(df0).mark_line().encode(
     x='date', y='streams_plays').properties(
    width=700,
    height=400,
    title="Aggregated listens longer than 60 seconds"
).configure_title(
    fontSize=20,
    font='Courier',
    anchor='start',
    color='white'
)
st.altair_chart(c)

df0["agg_followers"] = df0["followers"] + df0["New subscribers"]
df0 = df0[df0["New subscribers"] > -70]

c = alt.Chart(df0).mark_line().encode(
     x='date', y='agg_followers').properties(
    width=700,
    height=400,
    title="Aggregated followers"
).configure_title(
    fontSize=20,
    font='Courier',
    anchor='start',
    color='white'
)
st.altair_chart(c)

st.write(df0.streams_plays.describe())