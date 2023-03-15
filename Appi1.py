import pandas as pd 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt 

st.sidebar.markdown("## Side Panel")
st.sidebar.markdown("Use this panel to explore the dataset and create own viz.")
df = pd.read_csv("grates.csv")
    lowercase = lambda x:str(x).lower()
    df.rename(lowercase, axis='columns',inplace=True)
    return dfst.header("Now, Explore Yourself the Palmer Penguins")
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading palmerpenguins dataset...')
    # Load 10,000 rows of data into the dataframe.
df = load_data(100000)
    # Notify the reader that the data was successfully loaded.
data_load_state.text('Loading palmerpenguins dataset...Completed!')images=Image.open('images/meet.png')
st.image(images,width=600)
# Showing the original raw data
if st.checkbox("Show Raw Data", False):
    st.subheader('Raw data')
    st.write(df)st.title('Quick  Explore')
st.sidebar.subheader(' Quick  Explore')
st.markdown("Tick the box on the side panel to explore the dataset.")
if st.sidebar.checkbox('Basic info'):
    if st.sidebar.checkbox('Dataset Quick Look'):
        st.subheader('Dataset Quick Look:')
        st.write(df.head())
    if st.sidebar.checkbox("Show Columns"):
        st.subheader('Show Columns List')
        all_columns = df.columns.to_list()
        st.write(all_columns)
   
    if st.sidebar.checkbox('Statistical Description'):
        st.subheader('Statistical Data Descripition')
        st.write(df.describe())
    if st.sidebar.checkbox('Missing Values?'):
        st.subheader('Missing values')
        st.write(df.isnull().sum())