import pandas as pd
import pickle
from PIL import Image
import streamlit as st
import plotly.express as px


px.defaults.template = 'plotly_dark'
px.defaults.color_continuous_scale = 'reds'

#Menampilkan gambar pada sidebar
img = Image.open('asset/bike_share.png')
st.sidebar.image(img)

# Load dataset
with open ("day_data.pickle", 'rb') as f:
  data_day = pickle.load(f)

#Input tanggal
# min_date = data_day['dteday'].min()
# max_date = data_day['dteday'].max()
# start_date, end_date = st.sidebar.date_input(label='Rentang Waktu',
#                                              min_value=min_date,
#                                              max_value=max_date,
#                                              value=[min_date, max_date])

# Sidebar
st.sidebar.title("Bike Sharing Dashboard")

# Visualizations
st.title("Bike Sharing Dataset - Visualizations")

# # Custom Interactive Widget: Show Data
# st.sidebar.subheader("Show Raw Data")
# show_data = st.sidebar.checkbox("Display Raw Data")
# if show_data:
#     st.write(data_day)

# Custom Interactive Widget: Select Columns
st.sidebar.subheader("Select Columns")
selected_columns = st.sidebar.multiselect("Choose columns", data_day.columns)
if selected_columns:
    st.write(data_day[selected_columns])

# Custom Interactive Widget: Filter Data
st.sidebar.subheader("Filter Data")
selected_season = st.sidebar.selectbox("Select Season", data_day['season'].unique())
filtered_data = data_day[data_day['season'] == selected_season]

st.write(filtered_data)

# Bar chart: Count of Seasons
st.subheader("Count of Seasons")
season_count = data_day['season'].value_counts()
st.bar_chart(season_count)

# Filter data by year
filtered_year = st.sidebar.selectbox("Select Year", data_day['yr'].unique())
df_filtered_year = data_day[data_day['yr'] == filtered_year]

# Line chart: Correlation between Casual, Registered, and Count on Weekday
st.subheader(f"Correlation between Casual, Registered, and Count on Weekday (Year {filtered_year})")
avg_weekday_chart = df_filtered_year.groupby('weekday')[['casual', 'registered', 'cnt']].mean().plot(marker='o', linestyle='-', figsize=(10, 6))
st.pyplot(avg_weekday_chart.figure)

# Line chart: Average Count per Month
st.subheader("Correlation between Working Day and Year")
working_by_yr = data_day.groupby(['workingday', 'yr']).size().unstack()
st.bar_chart(working_by_yr)





# Custom analysis or visualizations based on your needs...

# Footer
st.sidebar.markdown('---')
st.sidebar.text('By: Farid Asroful A')
