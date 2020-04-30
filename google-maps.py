import gmaps 
import pandas as pd

gmaps.configure(api_key='your api key')

fig = gmaps.figure()
heatmap_layer = gmaps.heatmap_layer(
  df[['latitude','longitude']],
  weights=df['house_price'],
  max_intensity = 1000,
  point_radius=6.0
)

fig.add_layer(heatmap_layer)
fig
