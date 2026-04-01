import streamlit as st
import pandas as pd
from feeds import fetch_iocs

st.set_page_config(page_title="Threat Intel Dashboard")

st.title("Threat Intelligence Feed Integrator")
st.subheader("IOC Dashboard")

data = fetch_iocs()
df = pd.DataFrame(data)

st.metric("Total IOCs", len(df))

search = st.text_input("Search IOC")

if search:
    df = df[df["indicator"].str.contains(search, case=False)]

st.dataframe(df)

st.subheader("IOC Summary")
st.write(df["type"].value_counts())
