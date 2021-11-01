import streamlit as st
st.title("**Devos**")
st.subheader("Devos is an instagram page that shares data science , programming , tech news and courses and more")
st.title("Links")
st.subheader("Post :  first step to learn programming")
st.write(" [crash course computer science](https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo)")
st.video('https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo')
st.subheader("Post :  second step to learn programming ")
st.write("[python course in arabic](https://www.edraak.org/course/course-v1:PSUT+PL101+2018_SP/)")
st.write("[python coursera university of michigen](https://www.coursera.org/specializations/python)")
st.write("[free code camp python course in 4 hours](https://www.youtube.com/watch?v=rfscVS0vtbw&t=8137s)")
st.subheader('data viz : top 5 graphs in plotly')
st.write("jupyter notebook [github](https://github.com/amine-ziad-ounnoughene/devos/blob/main/graphs.ipynb)")
st.code("""## imshow

import plotly.express as px
from skimage import io
img = io.imread('https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Crab_Nebula.jpg/240px-Crab_Nebula.jpg')
fig = px.imshow(img)
fig.show()



## Geo data visualisation

import plotly.express as px
df = px.data.carshare()
fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                  mapbox_style="carto-positron")
fig.show()

## animation graphs

import plotly.express as px
df = px.data.gapminder()
px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

## time series

import plotly.express as px
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
fig = px.line(df, x='Date', y="AAPL.High")
fig.show()

## Pie charts

#to check more color palettes go to https://plotly.com/python/builtin-colorscales/
import plotly.express as px
df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent',color_discrete_sequence=px.colors.sequential.RdBu)
fig.show()""")
###

