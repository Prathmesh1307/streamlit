# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

@st.cache()
def load_data():
    # Load the Adult Income dataset into DataFrame.

    df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
    df.head()

    # Rename the column names in the DataFrame using the list given above. 

    # Create the list
    column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

    # Rename the columns using 'rename()'
    for i in range(df.shape[1]):
      df.rename(columns={i:column_name[i]},inplace=True)

    # Print the first five rows of the DataFrame
    df.head()

    # Replace the invalid values ' ?' with 'np.nan'.

    df['native-country'] = df['native-country'].replace(' ?',np.nan)
    df['workclass'] = df['workclass'].replace(' ?',np.nan)
    df['occupation'] = df['occupation'].replace(' ?',np.nan)

    # Delete the rows with invalid values and the column not required 

    # Delete the rows with the 'dropna()' function
    df.dropna(inplace=True)

    # Delete the column with the 'drop()' function
    df.drop(columns='fnlwgt',axis=1,inplace=True)

    return df

census_df = load_data()
st.set_option('deprecation.showPyplotGlobalUse', False)
# Write the code to design the web app
# Add title on the main page and in the sidebar.
# Add title on the main page and in the sidebar.
st.header("Census Data Visulization Web App")
st.sidebar.header("Menu")
# Using the 'if' statement, display raw data on the click of the checkbox.
if st.sidebar.checkbox("Show raw data"):
  st.subheader("Census Data set")
  st.dataframe(census_df)
  st.write(f"Number of rows : {census_df.shape[0]}")
  st.write(f"Number of columns : {census_df.shape[1]}")
# Add a multiselect widget to allow the user to select multiple visualisations.
# Add a subheader in the sidebar with the label "Visualisation Selector"
st.sidebar.subheader("Visualisation Selector")
# Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
# Store the current value of this widget in a variable 'plot_list'.
plot_types=st.sidebar.multiselect('Select the Charts/Plots:',('Box Plot', 'Count Plot', 'Pie Chart'))
# Display pie plot using matplotlib module and 'st.pyplot()'
if 'Pie Chart' in plot_types:
  st.subheader('Pie Chart')
  column_pie=st.sidebar.selectbox('Select the column to create a Pie Chart',("income","gender"))
  value_counts=census_df[column_pie].value_counts()
  plt.figure(figsize = (5,5))
  plt.title(f"Distribution of records for different {column_pie} groups")
  plt.pie(value_counts,labels=value_counts.index,autopct="%1.2f%%",explode=(0.2,0.0))
  st.pyplot() 
# Display box plot using matplotlib module and 'st.pyplot()'
if 'Box Plot' in plot_types:
  st.subheader('Box Plot for the Hours Worked Per Week')
  column_box=st.sidebar.selectbox('Select the column to create a box plot',("income","gender"))
  plt.title(f"Distribution of Hours Worked Per Week for different {column_box} groups")
  plt.figure(figsize = (12, 2))
  sns.boxplot(x="hours-per-week",y=column_box,data=census_df)
  st.pyplot() 
# Display count plot using seaborn module and 'st.pyplot()' 
if 'Count Plot' in plot_types:
  st.subheader('Count Plot for distribution of records for unique workclass groups')
  sns.countplot(x="workclass",data=census_df)
  st.pyplot() 