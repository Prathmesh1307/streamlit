# Import necessary modules 
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt 
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.header("Visualise Data")
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.subheader("Scatter plot")
  features_list = st.multiselect("Select the x-axis values:", ("carwidth","enginesize","horsepower","drivewheel_fwd","car_company_buick"))
  for feature in features_list:
    st.subheader(f"Scatter plot between {feature} and price")
    plt.figure(figsize = (12, 6))
    sns.scatterplot(x = feature, y = 'price', data = car_df)
    st.pyplot()
  st.subheader("Visulisation Selector")
  plot_types=st.multiselect('Select the Charts/Plots:',('Histogram', 'Box Plot', 'Correlation Heatmap'))
  if 'Histogram' in plot_types:
    st.subheader("Histogram")
    column=st.selectbox("Select the column to create a histogram",("carwidth","enginesize","horsepower","drivewheel_fwd","car_company_buick"))
    st.subheader(f"Histogram for {column}")
    plt.figure(figsize = (12, 2))
    plt.hist(car_df[column],bins="sturges")
    st.pyplot() 
  if 'Box Plot' in plot_types:
    st.subheader('Box Plot')
    column=st.selectbox("Select the column to create a Box Plot",("carwidth","enginesize","horsepower","drivewheel_fwd","car_company_buick"))
    st.subheader(f"Box plot for {column}")
    plt.figure(figsize = (12, 2))
    sns.boxplot(car_df[column])
    st.pyplot() 
  if 'Correlation Heatmap' in plot_types:
    st.subheader('Correlation Heatmap')
    plt.figure(figsize = (10,6))
    ax=sns.heatmap(car_df.corr(),annot=True)
    bottom,top=ax.get_ylim()
    ax.set_ylim(bottom+0.5,top-0.5)
    st.pyplot() 