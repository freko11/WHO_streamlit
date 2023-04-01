import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.set_page_config(page_title='WHO Life expectancy analysis',
                   page_icon=":bar_chart:",
                   layout="wide",
                   initial_sidebar_state='auto')

hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """

st.markdown(hide_st_style, unsafe_allow_html=True)


st.title("WHO Life expectancy dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('Life Expectancy Data.csv')
    df.columns = ['Country', 'Year', 'Status', 'Life expectancy', 'Adult Mortality',
                  'infant deaths', 'Alcohol', 'percentage expenditure', 'Hepatitis B',
                  'Measles', 'BMI', 'under-five deaths', 'Polio', 'Total expenditure',
                  'Diphtheria', 'HIV/AIDS', 'GDP', 'Population',
                  'thinness  1-19 years', ' thinness 5-9 years',
                  'Income composition of resources', 'Schooling']

    return df

df = load_data()

# Sidebar filters
sidebar = st.sidebar
countries = df["Country"].unique()
selected_country = sidebar.selectbox("Select a country", countries)
years = df["Year"].unique()
selected_year = sidebar.slider("Select a year", min_value=int(2000), max_value=int(2015), value=int(2015))

# Filter data based on selected filters
filtered_df = df[(df["Country"] == selected_country) & (df["Year"] == selected_year)]

# Display selected data in table
st.write(f"## {selected_country} Life Expectancy Data ({selected_year})")
st.write(filtered_df)


# Line chart showing life expectancy trend by country and year
st.write(f"## Life Expectancy Trends by Country and Year")
fig1 = px.line(df[df["Country"] == selected_country], x="Year", y="Life expectancy", color="Status")
fig1.update_layout(title=f"Life Expectancy Trend in {selected_country}", xaxis_title="Year",
                  yaxis_title="Life Expectancy")


fig2 = px.scatter(df[df["Year"] == selected_year], x="Life expectancy", y="GDP", color="Status", hover_name="Country")
fig2.update_layout(title=f"Life Expectancy vs. GDP per capita in {selected_year}", xaxis_title="Life Expectancy",
                  yaxis_title="GDP per capita")


left, right = st.columns(2)
left.plotly_chart(fig1, use_container_width=True)
right.plotly_chart(fig2, use_container_width=True)


fig3 = px.line(df[df["Country"] == selected_country], x="Year", y="Total expenditure", color="Status", hover_name="Country")
fig3.update_layout(title=f"Total expenditure on health over the years in {selected_country}", xaxis_title="Year",
                  yaxis_title="Total Expenditure")


fig4 = px.line(df[df["Country"] == selected_country], x="Year", y="Population", color="Status", hover_name="Country")
fig4.update_layout(title=f"Population over the years in {selected_country}", xaxis_title="Year",
                  yaxis_title="Population")


lefty, righty = st.columns(2)
lefty.plotly_chart(fig3, use_container_width=True)
righty.plotly_chart(fig4, use_container_width=True)