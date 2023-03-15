import streamlit as st 
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
import numpy as np 
import altair as alt 
import plotly.express as px
import base64


st.image("Gk.jpeg", width=80)
st.text("Giresse KIFOUANI")
st.text("Développeur Full stack et Data Analyst")

st.title("APPICATION ANALYSE DE DONNEES AVEC PYTHON ")

#st.markdown("Tuto essaie sur l'analyse de données avec la librairie Streamlit de python",unsafe_allow_html=True)
#st.markdown("Librairie utilisées : ",unsafe_allow_html=True)
#st.text("matplotlib")
#st.text("Pandas")
#st.text("Seaborn")
#st.text("Streamlit")"""
#st.image('GK.jpeg', caption = 'This is a picture', use_column_width = True)
add_selectbox = st.sidebar.selectbox(
    "Menu",
    ("Accueil", "DataFrame", "Afficher")
)

st.text("DONNEES SOUS FORMAT CSV")

f = st.sidebar.file_uploader("SELECTIONNEZ UN FICHIER SOUS FORMAT CSV ", ['csv'])


if f is not None:
	df = pd.read_csv(f)

	if st.sidebar.checkbox("Importer le fichier CSV", True):
		st.write(df)
		"---"

	if st.sidebar.checkbox("Visualisation graphique"):
		col = st.selectbox("Veuillez choisir une colonne de traitement																																																																			", df.columns)
		chart = alt.Chart(df).mark_line().encode(
			x=col,
			y="count()",
			).interactive()
		st.altair_chart(chart, use_container_width=True)




dff = pd.read_csv('sen_covid19.csv')


####st.write(dff)

st.text("DONNEES SOUS FORMAT EXCEL")
if st.checkbox('Afficher les données'):



	dff

if st.checkbox('Afficher le graphique'):
	coll = st.selectbox("Veuillez choisir une colonne de traitement", dff.columns)
	chart = alt.Chart(dff).mark_line().encode(
		x=coll,
		y="count()",
		).interactive()
	st.altair_chart(chart, use_container_width=True)


region = dff['REGION'].unique().tolist()
date = dff['DATE'].unique().tolist()

date = st.selectbox('Date', date, 100)

payss = st.multiselect('choisissez', region, ['Dakar'])

dff = dff[dff['REGION'].isin(payss)]
#dff = dff[dff['DATE']==date]

fig = px.bar(dff, x = "REGION", y="DECES", color="REGION", range_y=[0,35000], animation_frame="REGION", animation_group="DATE")

###fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 30
###fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5

fig.update_layout(width=800)
st.write(fig)